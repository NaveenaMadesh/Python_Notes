# def recursive_solution(problem):
#     """
#     STEP 1: IDENTIFY BASE CASE(S)
#     Ask: "When is the answer OBVIOUS and SIMPLE?"
#     - Could be n == 0, n == 1, empty list, etc.
#     - Can have MULTIPLE base cases!
#     """
#     if simple_condition_1:
#         return obvious_answer_1
#     if simple_condition_2:
#         return obvious_answer_2
    
#     """
#     STEP 2: MAKE PROBLEM SMALLER
#     Common patterns:
#     - Numbers: n-1, n//2
#     - Strings: s[1:], s[:-1]
#     - Lists: lst[1:], lst[:-1]
#     """
    
#     """
#     STEP 3: DO TINY WORK (Optional)
#     - BEFORE recursive call = happens going DOWN
#     - AFTER recursive call = happens coming BACK UP
#     """
#     work_before()  # Optional
    
#     """
#     STEP 4: TRUST THE RECURSION
#     Call yourself with SMALLER problem
#     Can have MULTIPLE recursive calls!
#     """
#     result1 = recursive_solution(smaller_problem_1)
#     result2 = recursive_solution(smaller_problem_2)  # Optional
    
#     """
#     STEP 5: COMBINE & RETURN
#     Combine your work with recursive results
#     """
#     work_after()  # Optional
    
#     return combine(my_work, result1, result2)