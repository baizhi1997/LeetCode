
| [English](README_EN.md) | 简体中文 |

# [85. 最大矩形](https://leetcode-cn.com/problems/maximal-rectangle/)

## 题目描述

<p>给定一个仅包含 <code>0</code> 和 <code>1</code> 、大小为 <code>rows x cols</code> 的二维二进制矩阵，找出只包含 <code>1</code> 的最大矩形，并返回其面积。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg" style="width: 402px; height: 322px;" />
<pre>
<strong>输入：</strong>matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
<strong>输出：</strong>6
<strong>解释：</strong>最大矩形如上图所示。
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>matrix = []
<strong>输出：</strong>0
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>matrix = [["0"]]
<strong>输出：</strong>0
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>matrix = [["1"]]
<strong>输出：</strong>1
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>matrix = [["0","0"]]
<strong>输出：</strong>0
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>rows == matrix.length</code></li>
	<li><code>cols == matrix.length</code></li>
	<li><code>0 <= row, cols <= 200</code></li>
	<li><code>matrix[i][j]</code> 为 <code>'0'</code> 或 <code>'1'</code></li>
</ul>


## 相关话题

- [栈](https://leetcode-cn.com/tag/stack)
- [数组](https://leetcode-cn.com/tag/array)
- [哈希表](https://leetcode-cn.com/tag/hash-table)
- [动态规划](https://leetcode-cn.com/tag/dynamic-programming)

## 相似题目

- [柱状图中最大的矩形](../largest-rectangle-in-histogram/README.md)
- [最大正方形](../maximal-square/README.md)
