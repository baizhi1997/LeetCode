
| English | [简体中文](README.md) |

# [241. Different Ways to Add Parentheses](https://leetcode-cn.com/problems/different-ways-to-add-parentheses/)

## Description

<p>Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are <code>+</code>, <code>-</code> and <code>*</code>.</p>

<p><b>Example 1:</b></p>

<pre>
<b>Input:</b> <code>&quot;2-1-1&quot;</code>
<b>Output:</b> <code>[0, 2]</code>
<strong>Explanation: </strong>
((2-1)-1) = 0 
(2-(1-1)) = 2</pre>

<p><b>Example 2:</b></p>

<pre>
<b>Input: </b><code>&quot;2*3-4*5&quot;</code>
<b>Output:</b> <code>[-34, -14, -10, -10, 10]</code>
<strong>Explanation: 
</strong>(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10<strong>
</strong></pre>

## Related Topics

- [Divide and Conquer](https://leetcode-cn.com/tag/divide-and-conquer)

## Similar Questions

- [Unique Binary Search Trees II](../unique-binary-search-trees-ii/README_EN.md)
- [Basic Calculator](../basic-calculator/README_EN.md)
- [Expression Add Operators](../expression-add-operators/README_EN.md)
