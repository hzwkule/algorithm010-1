学习笔记

分治
       problem
      /       \
  subproblem  subproblem
  
  def divide_conquer(problem, param1, param2, ...):
    #recursion terminator
    if problem is None:
      print_result
      return
    
    #prepare data
    data = prepare_data(problem)
    subproblems = split_problem(problem, data)
    
    #conquer subproblems
    subresult1 = self.divide_conquer(subproblem[0], p1, ..)
    subresult2 = self.divide_conquer(subproblem[1], p1, ..)
    subresult3 = self.divide_conquer(subproblem[2], p1, ..)
   
    #process and generate the final result
    result = process_result(subresult1, subresult2, subresult3, ...)
    
    #revert current level status
回溯

递归
  //-1.terminatoer
  if (level > MAX_LEVEL) {
    //process result
    return
  }
  //2.process
  process(level, param)
  //3.drill down
  recur(level: level+1, newParam)
  //4.restore current status
动态规划 -- 分治+最优子结构
  共性：找重复子问题
  差异性：最优子结构、中途可以淘汰次优解
  1.子问题（最优子结构）
  2.储存中间状态
  3.状态转移方程
  
本质：寻找重复性-->计算机指令集
形成机器思维
