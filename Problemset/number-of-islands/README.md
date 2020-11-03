
| [English](README_EN.md) | 简体中文 |

# [200. 岛屿数量](https://leetcode-cn.com/problems/number-of-islands/)

## 题目描述

<p>给你一个由 <code>'1'</code>（陆地）和 <code>'0'</code>（水）组成的的二维网格，请你计算网格中岛屿的数量。</p>

<p>岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。</p>

<p>此外，你可以假设该网格的四条边均被水包围。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
<strong>输出：</strong>1
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
<strong>输出：</strong>3
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>m == grid.length</code></li>
	<li><code>n == grid[i].length</code></li>
	<li><code>1 <= m, n <= 300</code></li>
	<li><code>grid[i][j]</code> 的值为 <code>'0'</code> 或 <code>'1'</code></li>
</ul>


## 相关话题

- [深度优先搜索](https://leetcode-cn.com/tag/depth-first-search)
- [广度优先搜索](https://leetcode-cn.com/tag/breadth-first-search)
- [并查集](https://leetcode-cn.com/tag/union-find)

## 相似题目

- [被围绕的区域](../surrounded-regions/README.md)
- [墙与门](../walls-and-gates/README.md)
- [岛屿数量 II](../number-of-islands-ii/README.md)
- [无向图中连通分量的数目](../number-of-connected-components-in-an-undirected-graph/README.md)
- [不同岛屿的数量](../number-of-distinct-islands/README.md)
- [岛屿的最大面积](../max-area-of-island/README.md)
