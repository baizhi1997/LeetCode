
# @Title: 有效电话号码 (Valid Phone Numbers)
# @Author: qinxinlei
# @Date: 2018-11-16 15:21:07
# @Runtime: 8 ms
# @Memory: N/A

# Read from the file file.txt and output all valid phone numbers to stdout.
grep -P '^(\d{3}-|\(\d{3}\) )\d{3}-\d{4}$' file.txt
