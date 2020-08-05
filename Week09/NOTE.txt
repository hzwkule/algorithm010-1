学习笔记

递归、分治、回溯、动态规划复习

递归
public void recur(int level, int param) {
  //terminator
  if (level < MAX_LEVEL) {
    //process result
    return;
  }
  
  //process current logic
  process(level, param);
  
  //drill down
  recur(level: level + 1, newParam);
  
  //restore current status
}

分而治之
def divide_conquer(problem, param1, param2, ...):
  # recursion terminator
  if problem is None:
    print_result
    return
    
  # prepare data
  data = prepare_data(problem)
  subproblems = split_problem(problem, data)
  
  # conquer subproblems
  subresult1 = self.divide_conquere(subproblems[0], p1, ...)
  subresult2 = self.divide_conquere(subproblems[2], p1, ...)
  subresult3 = self.divide_conquere(subproblems[3], p1, ...)
  ...
  
  # process and generate the final result
  result = process_result(subresult1, subresult2, subresult3, ...)
  
  # revert the current level states
  
感触
1.人肉递归低效、很累
2.找到最近最简方法，将其拆解成可重复解决的问题
3.数学归纳法思维
本质：寻找重复性-->计算机指令集

动态规划
1."Simplifying a complicated problem by breaking it down into simpler sub-problems"
  (in a recursive manner)
2.Divide & Conquer + Optimal substructure
  分治 + 最优子结构
3.顺推形式：动态递推

function DP():
  dp = [][] #二维情况
  
  for i = 0 .. M {
    for j = 0 .. N {
      dp[i][j] = _Function(dp[i'][j']...)
    }
  }
  
  return dp[M][N]
关键点
动态规划 和 递归或者分治 没有根本上的区别（关键看有无最优的子结构）
拥有共性：找到重复子问题
差异性：最优子结构、中途可以淘汰次优解

高阶的DP问题

复杂度来源
1.状态拥有更多维度（二维、三维、或者更多、甚至需要压缩）
2.状态方程更加复杂
本质：内功、逻辑思维、数学


字符串基础知识

字符串
-Python
  x='abbc'
  x="abbc"
-Java
  String x = "abbc";
-C++:
  string x("abbc")

遍历字符串
-Python
  for ch in "abbc":
    print(ch)
-Java
  String x = "abbc"
  for (int i = 0; i < x.size(); ++i) {
    char ch = x.charAt(i);
  }
  for ch in x.toCharArray() {
    System.out.println(ch);
  }
-C++
  string x("abbc")
  for (int i = 0; i < x.length(); i++) {
    cout << x[i];
  }
  
字符串比较
Java
  String x = "abb";
  String y = "abb";
  
  x == y --> false
  
  x.equals(y) --> true
  x.equalsIgnoreCase(y) --> true
  
字符串相关算法
  atoi
  public int myAtoi(String str) {
    int index = 0, sign = 1, total = 0;
    //1. Empty string
    if (str.length() == 0) return 0;
    
    //2. Remove Spaces
    while (str.charAt(index) == '' && index < str.length())
      index++;
      
    //3. Handle signs
    if (str.charAt(index) == '+' || str.charAt(index) == '-') {
      sign = str.charAt(index) == '+' ? 1 : -1;
      index++;
    }
    
    //4. Convert number and avoid overflow
    while (index < str.length()) {
      int digit = str.charAt(index) - '0';
      if (digit < 0 || digit > 9) break;
      
      // check if total will be overflow after 10 times and add digit
      if (Interger.MAX_VALUE/10 < total ||
          Interger.MAX_VALUE/10 == total && Interger.MAX_VALUE % 10 < digit)
          return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
      total = 10 * total + digit;
      index++;
    }
    return total * sign;
  }
  
    class Solution(object):
      
      def myAtoi(self, s):
        if len(s) == 0: return 0
        ls = list(s.strip())
        
        sign = -1 if ls[0] == '-' else 1
        
        if ls[0] in ['-','+']: del ls[0]
        
        ret, i = 0, 0
        
        while i < len(ls) and ls[i].isdigit():
          ret = ret*10 + ord(ls[i]) - ord('0')
          i += 1
        return max(-2**31, min(sign*ret, 2**31-1))
        
高级字符串算法
1. Longest common seequence (最长子序列）

2. Longest common substring (最长子串）

3. Edit distance (编辑距离）
  
字符串匹配算法
1.暴力法（brute force） O(mn)
2.Rabin-Karp 算法
3.KMP 算法
  
  
  
  
  
  
  
  
  
  
  
  
