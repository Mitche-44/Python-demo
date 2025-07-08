## 1.Company Emails Var (Quartz variant)
100 points

You are given a list of names of new employees in a company. You need to generate a company email address for each of them.
The name of each person consists of two or three parts: a first name, an optional middle name, and a last name, separated by spaces. Each part can include only English letters (but the last name may additionally contain hyphens). The name of the company also consists only of English letters.
Each address must use the format "FirstMiddleLast@Company.com" where
First is the initial of the first name,
Middle is the initial of the middle name (but only if the person has a middle name),
Last is the last name, truncated to at most 8 initial letters,
Company is the company name.
The address should be in lower case and should not contain hyphens.
Note that hyphens should be removed before truncating the last name.
Additionally, if more than one person would have the same email address, differentiate their addresses by adding subsequent integers (starting from the second address and number 2) before the "@" sign. For example, if there are three people who would have the address "jd@company.com", they should be assigned addresses "jd@company.com", "jd2@company.com" and "jd3@company.com" respectively.
Write a function:
function solution(S, C);
that, given a string S containing a list of names separated by the characters ", "
(a comma followed by a space)
and a string C specifying the name of the company, returns a string containing the list of email addresses separated by the characters ", " in the same order as they were in the input. Each entry on the list should be of the form "Name <Email>".
For example, given C = "Example" and string S as follows:
"John Doe, Peter Parker, Mary Jane Watson-Parker, James Doe, John Elvis Doe, Jane Doe, Penny Parker"
the function should return:
"John Doe <jdoe@example.com>, Peter Parker <pparker@example.com>, Mary Jane Watson-Parker <mjwatsonpa@example.com>, James Doe <jdoe2@example.com>, John Elvis Doe <jedoe@example.com>, Jane Doe <jdoe3@example.com>, Penny Parker <pparker2@example.com>".
Assume that:
the length of string S is within the range [3..1,000];
the length of string C is within the range [1..100];
string S consists only of letters (a−z and/or A−Z), spaces, hyphens and commas;
string S contains valid names; no name appears more than once;
string C is made only of letters (a−z and/or A−Z).

## 2.Different Letters Concatenation

100 points

Concatenation is an operation that joins strings. For example, the concatenation of strings "smart" and "phone" is "smartphone". Concatenation can be expanded to more than two strings; for example, concatenating "co", "dil" and "ity" results in "codility".
Given an array A consisting of strings, your function should calculate the length of the longest string S such that:
S is a concatenation of some of the strings from A;
every letter in S is different.
Write a function:
function solution(A);
that, given an array A consisting of N strings, calculates the length of the longest string S fulfilling the conditions above. If no such string exists, your function should return 0.
Examples:
1. Given A = ["co", "dil", "ity"], your function should return 5. The resulting string S could be "codil", "dilco", "coity" or "ityco".
2. Given A = ["abc", "yyy", "def", "csv"], your function should return 6. The resulting string S could be "abcdef", "defabc", "defcsv" or "csvdef".
3. Given A = ["potato", "kayak", "banana", "racecar"], your function should return 0. It is impossible to choose any of these strings as each of them contains repeating letters.
4. Given A = ["eva", "jqw", "tyn", "jan"], your function should return 9. One of the possible strings of this length is "evajqwtyn".
Assume that:
N is an integer within the range [1..8];
each string in A consists of lowercase English letters;
the sum of lengths of strings in A does not exceed 100.