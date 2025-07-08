## 1. Company Emails Var (Quartz variant)
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

The function should return:

"John Doe <jdoe@example.com>, Peter Parker <pparker@example.com>, Mary Jane Watson-Parker <mjwatsonpa@example.com>, James Doe <jdoe2@example.com>, John Elvis Doe <jedoe@example.com>, Jane Doe <jdoe3@example.com>, Penny Parker <pparker2@example.com>".

Assume that:

- the length of string S is within the range [3..1,000];

- the length of string C is within the range [1..100];

- string S consists only of letters (a−z and/or A−Z), spaces, hyphens and commas;

- string S contains valid names; no name appears more than once;

- string C is made only of letters (a−z and/or A−Z).

## 2. Different Letters Concatenation

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

- N is an integer within the range [1..8];

- each string in A consists of lowercase English letters;

- the sum of lengths of strings in A does not exceed 100.


## 3. Even Word

100 points

In an even word, each letter occurs an even number of times.
Write a function solution that, given a string S consisting of N characters, returns the minimum number of letters that must be deleted to obtain an even word.
Examples:
1. Given S = "acbcbba", the function should return 1 (one letter b must be deleted).
2. Given S = "axxaxa", your function should return 2 (one letter a and one letter x must be deleted).
3. Given S = "aaaa", your function should return 0 (there is no need to delete any letters).

Write an efficient algorithm for the following assumptions:

- N is an integer within the range [0..200,000];

- string S is made only of lowercase letters (a−z)

## 4. Pair Of Two Digit Numbers

100 points

You are given a string S consisting of N digits. What is the largest sum of two two-digit fragments of S? The selected fragments cannot overlap.
Write a function:
def solution(S)
that, given a string S, returns the largest sum of two two-digit numbers that are non-overlapping fragments of S.
Examples:
1. Given S = "43798", the function should return 141. The chosen fragments are "43" and "98": "43 7 98"
2. Given S = "00101", the function should return 10. The chosen fragments are "00" and "10": "00 10 1". Note that fragments "01" and "10" cannot be chosen as they overlap.
3. Given S = "0332331", the function should return 66. The chosen fragments are "33" and "33": "0 33 2 33 1".
4. Given S = "00331", the function should return 34. The chosen fragments are "03" and "31": "0 03 31"

Assume that:

- N is an integer within the range [4..100];

- string S is made only of digits (0−9).

## 5. XY Split

100 points

You are given a string S consisting of N lowercase English letters. In how many ways can we split S into two non-empty parts, such that in at least one part the letter 'x' and the letter 'y' occur the same number of times?
Write a function:
function solution(S);
that, given a string S of length N, returns the number of splits S satisfying the condition above.
Examples:
1. Given S = "ayxbx", the function should return 3. There are four possible splits of S: "a/yxbx", "ay/xbx", "ayx/bx" and "ayxb/x". Only "ay/xbx" does not fulfill the condition, so the answer is 3. Note that in "a/yxbx" the left part has 0 occurrences of 'x' and 'y', so it counts as correct split.
2. Given S = "xzzzy", the function should return 0.
3. Given S = "toyxmy", the function should return 5.
4. Given S = "apple", the function should return 4.

Write an efficient algorithm for the following assumptions:

- N is an integer within the range [2..200,000];

- string S is made only of lowercase letters (a−z).

## 6. Create Palindrome

100 points

Write a function solution that, given a string S of length N, returns any palindrome which can be obtained by replacing all of the question marks in S by lowercase letters ('a'−'z'). If no palindrome can be obtained, the function should return the string "NO".
A palindrome is a string that reads the same both forwards and backwards. Some examples of palindromes are: "kayak", "radar", "mom".
Examples:
1. Given S = "?ab??a", the function should return "aabbaa".
2. Given S = "bab??a", the function should return "NO".
3. Given S = "?a?", the function may return "aaa". It may also return "zaz", among other possible answers. The function is supposed to return only one of the possible answers.

Assume that:

- N is an integer within the range [1..1,000];

- string S consists only of lowercases letters ('a' − 'z') or '?'.

## 7. Asphalt Patches

100 points

There is a road consisting of N segments, numbered from 0 to N-1, represented by a string S. Segment S[K] of the road may contain a pothole, denoted by a single uppercase "X" character, or may be a good segment without any potholes, denoted by a single dot, ".".
For example, string ".X..X" means that there are two potholes in total in the road: one is located in segment S[1] and one in segment S[4]. All other segments are good.
The road fixing machine can patch over three consecutive segments at once with asphalt and repair all the potholes located within each of these segments. Good or already repaired segments remain good after patching them.
Your task is to compute the minimum number of patches required to repair all the potholes in the road.
Write a function:
function solution(S);
that, given a string S of length N, returns the minimum number of patches required to repair all the potholes.
Examples:
1. Given S = ".X..X", your function should return 2. The road fixing machine could patch, for example, segments 0-2 and 2-4.
2. Given S = "X.XXXXX.X.", your function should return 3. The road fixing machine could patch, for example, segments 0-2, 3-5 and 6-8.
3. Given S = "XX.XXX..", your function should return 2. The road fixing machine could patch, for example, segments 0-2 and 3-5.
4. Given S = "XXXX", your function should return 2. The road fixing machine could patch, for example, segments 0-2 and 1-3.

Write an efficient algorithm for the following assumptions:

- N is an integer within the range [3..100,000];

- string S is made only of the characters '.' and/or 'X'.

## 8. Sanitorium Accomodation

100 points

There are N guests (numbered from 0 to N-1) in a sanatorium waiting to be assigned a room. In each room, any number of guests can be accommodated. However, not all guests like to have a lot of roommates.
You are given an array A of N integers: the K-th guest wants to be in a room that contains at most A[K] guests, including themselves.
Write a function:
def solution(A)
that, given the array A, returns the minimum number of rooms needed to accommodate all guests.
Examples:
1. Given A = [1, 1, 1, 1, 1], your function should return 5. Each guest should be accommodated in their own separate room.
2. Given A = [2, 1, 4], your function should return 2. The second guest should be accommodated in one room and the other two guests in another room.
3. Given A = [2, 7, 2, 9, 8], your function should return 2. The first and the third guests should be accommodated in one room and the other three guests in another room.
4. Given A = [7, 3, 1, 1, 4, 5, 4, 9], your function should return 4. The guests can be accommodated as follows: the first two guests in one room, the third and the fourth guests in two single rooms, and the other guests in another room.

Write an efficient algorithm for the following assumptions:
- N is an integer within the range [1..100,000];
- each element of array A is an integer within the range [1..100,000].


## 9. Dice Rolls

100 points

You have just rolled a dice several times. The N roll results that you remember are described by an array A. However, there are F rolls whose results you have forgotten. The arithmetic mean of all of the roll results (the sum of all the roll results divided by the number of rolls) equals M.
What are the possible results of the missing rolls?
Write a function:
def solution(A, F, M)
that, given an array A of length N, an integer F and an integer M, returns an array containing possible results of the missed rolls. The returned array should contain F integers from 1 to 6 (valid dice rolls). If such an array does not exist then the function should return [0].
Examples:
1. Given A = [3, 2, 4, 3], F = 2, M = 4, your function should return [6, 6]. The arithmetic mean of all the rolls is (3 + 2 + 4 + 3 + 6 + 6) / 6 = 24 / 6 = 4.
2. Given A = [1, 5, 6], F = 4, M = 3, your function may return [2, 1, 2, 4] or [6, 1, 1, 1] (among others).
3. Given A = [1, 2, 3, 4], F = 4, M = 6, your function should return [0]. It is not possible to obtain such a mean.
4. Given A = [6, 1], F = 1, M = 1, your function should return [0]. It is not possible to obtain such a mean.

Write an efficient algorithm for the following assumptions:
- N and F are integers within the range [1..100,000];
- each element of array A is an integer within the range [1..6];
- M is an integer within the range [1..6].