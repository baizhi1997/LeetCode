
| [English](README_EN.md) | 简体中文 |

# [76. 最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring/)

## 题目描述

<p>给你一个字符串 <code>s</code> 、一个字符串 <code>t</code> 。返回 <code>s</code> 中涵盖 <code>t</code> 所有字符的最小子串。如果 <code>s</code> 中不存在涵盖 <code>t</code> 所有字符的子串，则返回空字符串 <code>""</code> 。</p>

<p><strong>注意：</strong>如果 <code>s</code> 中存在这样的子串，我们保证它是唯一的答案。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>s = "ADOBECODEBANC", t = "ABC"
<strong>输出：</strong>"BANC"
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>s = "a", t = "a"
<strong>输出：</strong>"a"
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 <= s.length, t.length <= 10<sup>5</sup></code></li>
	<li><code>s</code> 和 <code>t</code> 由英文字母组成</li>
</ul>

<p> </p>
<strong>进阶：</strong>你能设计一个在 <code>o(n)</code> 时间内解决此问题的算法吗？

## 相关话题

- [哈希表](https://leetcode-cn.com/tag/hash-table)
- [双指针](https://leetcode-cn.com/tag/two-pointers)
- [字符串](https://leetcode-cn.com/tag/string)
- [None](https://leetcode-cn.com/tag/sliding-window)

## 相似题目

- [串联所有单词的子串](../substring-with-concatenation-of-all-words/README.md)
- [长度最小的子数组](../minimum-size-subarray-sum/README.md)
- [滑动窗口最大值](../sliding-window-maximum/README.md)
- [字符串的排列](../permutation-in-string/README.md)
- [最小窗口子序列](../minimum-window-subsequence/README.md)
