
#!/usr/bin/env python3
import string
import sys
import time
from concurrent.futures import ProcessPoolExecutor, as_completed


def f_val(byte):
    """
    Given a byte (after XOR with key), splits it into four 2‐bit chunks and returns
    the sum of contributions based on:
       0 -> -35, 1 -> +1, 2 -> +35, 3 -> -1.
    """
    mapping = {0: -35, 1: 1, 2: 35, 3: -1}
    return sum(mapping[(byte >> shift) & 3] for shift in range(0, 8, 2))

TARGET_TOTAL = 1152  # Because starting at 36, we need to add 1152 to reach 1188. (which was found from static analysis)
fixed_positions = {0: 'C', 1: 'T', 2: 'F', 3: '{', 20: '}'}
# Key bytes from the binary (positions 0..20).
keys = [
    0x19, 0x0e, 0xe3, 0x2e, 0xc9, 0x89, 0xc9, 0x61, 0xd5, 0x69,
    0x05, 0x34, 0x65, 0x27, 0x7b, 0x05, 0x69, 0xc8, 0x98, 0x99, 0x28
]
allowed_chars = list(string.ascii_letters)
# Unknown flag positions (global indices) are from 4 to 19.
unknown_indices = list(range(4, 20))

# These globals will be computed in __main__ and then used by worker functions.
candidate_table = None
cum_min = None
cum_max = None
n = None
target_unknown = None

def dfs_slice(pos, current_sum):
    """
    Recursively assigns candidate letters for candidate_table positions [pos, n)
    so that current_sum plus the contributions from later positions equals target_unknown.
    Returns a list of chosen letters if a solution is found; otherwise, returns None.
    """
    global candidate_table, cum_min, cum_max, n, target_unknown
    if pos == n:
        return [] if current_sum == target_unknown else None
    if current_sum + cum_max[pos] < target_unknown or current_sum + cum_min[pos] > target_unknown:
        return None
    for ch, val in candidate_table[pos]:
        new_sum = current_sum + val
        if new_sum + cum_max[pos+1] < target_unknown or new_sum + cum_min[pos+1] > target_unknown:
            continue
        res = dfs_slice(pos + 1, new_sum)
        if res is not None:
            return [ch] + res
    return None

def worker(first_candidate):
    """
    Worker function to process one candidate for the first unknown position.
    first_candidate is a tuple (ch, contribution) for candidate_table[0] (which corresponds to global flag index 4).
    It runs DFS for positions 1 .. n-1 starting with the candidate's contribution.
    Returns a list of chosen letters (of length n) if a valid solution is found; otherwise returns None.
    """
    ch, val = first_candidate
    sol_rest = dfs_slice(1, val)
    if sol_rest is not None:
        return [ch] + sol_rest
    return None


if __name__ == "__main__":
    start_time = time.time()
    
    fixed_sum = 0
    for pos, ch in fixed_positions.items():
        fixed_sum += f_val(ord(ch) ^ keys[pos])
    target_unknown = TARGET_TOTAL - fixed_sum
    # For our fixed positions, fixed_sum should be 224, so target_unknown should be 928.
    print(f"Fixed sum: {fixed_sum}  Target for unknown positions: {target_unknown}")
    
    candidate_table = []
    ideal = target_unknown / len(unknown_indices)
    for global_pos in unknown_indices:
        candidates = []
        for ch in allowed_chars:
            contrib = f_val(ord(ch) ^ keys[global_pos])
            candidates.append((ch, contrib))
        candidates.sort(key=lambda pair: abs(pair[1] - ideal))
        candidate_table.append(candidates)
    
    n = len(candidate_table)  # should be 16.
    min_table = [min(val for _, val in cand) for cand in candidate_table]
    max_table = [max(val for _, val in cand) for cand in candidate_table]
    cum_min = [0] * (n + 1)
    cum_max = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        cum_min[i] = cum_min[i + 1] + min_table[i]
        cum_max[i] = cum_max[i + 1] + max_table[i]
    
    total_first_candidates = len(candidate_table[0])
    solution = None
    with ProcessPoolExecutor() as executor:
        futures = {executor.submit(worker, cand): cand for cand in candidate_table[0]}
        finished = 0
        for future in as_completed(futures):
            finished += 1
            print(f"\rFinished {finished}/{total_first_candidates} tasks", end="", flush=True)
            try:
                res = future.result()
            except Exception as e:
                print("\nException in worker:", e, file=sys.stderr)
                continue
            if res is not None:
                solution = res
                break
    elapsed = time.time() - start_time
    print()
    
    if solution is not None:
        flag_chars = [''] * 21
        for pos, ch in fixed_positions.items():
            flag_chars[pos] = ch
        for letter, global_idx in zip(solution, unknown_indices):
            flag_chars[global_idx] = letter
        flag_str = "".join(flag_chars)
        print(f"Flag found {flag_str}")
        print(f"time: {elapsed:.2f} seconds")
    else:
        print("No solution")
