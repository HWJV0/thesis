"""
Original Paper: https://arxiv.org/abs/2103.03874
Paper Repository: https://github.com/hendrycks/math
"""

MATH_NUMBERTHEORY_FEWSHOT_EXAMPLES_AGENT_COT = {
    "Level 1": """Question: What is the remainder when (99)(101) is divided by 9?
Thought: Notice that when we divide (99)(101) by 9, we get $\\frac{99\\cdot101}{9}=11\\cdot101$. The quotient is an integer and there is no remainder, so (99)(101) is a multiple of 9 and the remainder is $\\boxed{0}$.\n\nOR\n\nWe notice that $99\\cdot101=99\\cdot100+99=9999$. We can easily see that 9999 is divisible by 9, as the division results in 1111 with a remainder of 0. Alternatively, a number is divisible by 9 if the sum of its digits is a multiple of 9. In this case, the sum of the digits in 36, a multiple of 9, so 9999 is a also a multiple of 9. That means the remainder when it is divided by 9 is $\\boxed{0}$.
Action: Finish[\\boxed{0}]


Question: What is the smallest positive integer that ends in 9 and is divisible by 7?
Thought: We can start from 9 and keeping adding 10 until we reach an integer divisible by 7. It turns out that 9, 19, 29, and 39 are all not divisible by 7, but 49 is divisible by 7. Therefore, $\\boxed{49}$ is the smallest integer that ends in a 9 and is divisible by 7.
Action: Finish[\\boxed{49}]


Question: When Joyce counts the pennies in her bank by fives, she has one left over. When she counts them by threes, there are two left over. What is the least possible number of pennies in the bank?
Thought: Let $a$ be the least number of pennies that Joyce could have in the bank. Then \\begin{align*}\na & \\equiv 1\\pmod 5\\\\\na & \\equiv 2\\pmod 3\n\\end{align*} The first few positive solutions to $a\\equiv 1\\pmod 5$ are $1,6,11$. Luckily, while the first two do not satisfy $a\\equiv 2\\pmod 3$, $\\boxed{11}$ does!
Action: Finish[\\boxed{11}]


Question: What is the greatest possible number of digits in the product of a 4-digit whole number and a 3-digit whole number?
Thought: The greatest product of a 4-digit whole number and a 3-digit whole number is $(10^4-1)(10^3-1)=10^7-10^4-10^3+1=10^7-(10^4+10^3-1)$. $10^7$ has 8 digits and $10^4+10^3-1=11,000-1=10,999$ has 5 digits. Clearly, their difference (10,000,000-10,999) has $8-1=\\boxed{7}$ digits.
Action: Finish[\\boxed{7}]


Question: When three positive integers are divided by $12$, the remainders are $7,$ $9,$ and $10,$ respectively.\n\nWhen the sum of the three integers is divided by $12$, what is the remainder?
Thought: We can call the three integers in this problem $a,$ $b,$ and $c$. Then we have \\begin{align*}\na &\\equiv 7\\pmod{12}, \\\\\nb &\\equiv 9\\pmod{12}, \\\\\nc &\\equiv 10\\pmod{12}.\n\\end{align*}Adding these congruences, we have \\begin{align*}\na+b+c &\\equiv 7+9+10 \\\\\n&= 26\\pmod{12}.\n\\end{align*}Therefore, $a+b+c$ has the same remainder as $26$ upon division by $12$. This remainder is $\\boxed{2}$.
Action: Finish[\\boxed{2}]""",

    "Level 2": """Question: For the opening home game of the baseball season, the Madd Batters minor league baseball team offered the following incentives to its fans:\n\nEvery 75th fan who entered the stadium got a coupon for a free hot dog.\n\nEvery 30th fan who entered the stadium got a coupon for a free cup of soda.\n\nEvery 50th fan who entered the stadium got a coupon for a free bag of popcorn.\n\nThe stadium holds 4000 fans and was completely full for this game. How many of the fans at the game were lucky enough to receive all three free items?
Thought: We are asked to count the common multiples of $\\{75,30,50\\}$ among the positive integers less than or equal to $4000$.  Since $75=3\\cdot 5^2$, $30=2\\cdot3\\cdot 5$, and $50=2\\cdot 5^2$, the least common multiple of the three numbers is $2\\cdot 3 \\cdot 5^2=150$.  Since every common multiple is divisible by the least common multiple, we may count the multiples of $150$ less than $4000$. We divide $4000$ by $150$ and find a quotient of $\\boxed{26}$.
Action: Finish[\\boxed{26}]


Question: The number 210 is the product of two consecutive positive integers and is also the product of three consecutive integers. What is the sum of those five integers?
Thought: First we prime factorize $210=2\\cdot3\\cdot5\\cdot7$. Trying some pairwise products of these primes, we see that $210=(2\\cdot7)(3\\cdot5)=14\\cdot15$. Also, $210=(5)(2\\cdot3)(7)=5\\cdot6\\cdot7$. The sum of the five integers is $14+15+5+6+7=\\boxed{47}$.
Action: Finish[\\boxed{47}]


Question: There is a unique two-digit positive integer $t$ for which the last two digits of $11\\cdot t$ are $36$.\n\nWhat is $t$?
Thought: We can write the condition on $t$ as $$11\\cdot t \\equiv 36\\pmod{100}.$$Then, multiplying both sides by $9$, we have $$99\\cdot t \\equiv 324 \\equiv 24\\pmod{100}.$$The left side, $99t$, is congruent modulo $100$ to $-t$, so we have $$-t \\equiv 24\\pmod{100}$$and therefore $$t \\equiv -24\\pmod{100}.$$The unique two-digit positive solution is $t=-24+100=\\boxed{76}$. Indeed, we can check that $11\\cdot 76 = 836$, which does end in $36$.
Action: Finish[\\boxed{76}]


Question: Suppose $77\\cdot 88\\cdot 99 \\equiv n\\pmod{20}$, where $0\\le n<20$.\n\nWhat is the value of $n$?
Thought: We begin by reducing the factors of the product modulo 20: \\begin{align*}\n77 &\\equiv -3\\pmod{20},\\\\\n88 &\\equiv 8\\pmod{20},\\\\\n99 &\\equiv -1\\pmod{20}.\n\\end{align*}(Note that we could have used the more \"standard\" reductions $77\\equiv 17$ and $99\\equiv 19$, but the reductions above will make our computations easier.)\n\nNow we have \\begin{align*}\n77\\cdot 88\\cdot 99 &\\equiv (-3)\\cdot 8\\cdot(-1) \\\\\n&= 24 \\\\\n&\\equiv \\boxed{4}\\pmod{20}.\n\\end{align*}
Action: Finish[\\boxed{4}]


Question: How many positive factors of 72 are perfect cubes?
Thought: Prime factorize $72$ as $2^3\\cdot 3^2$.  A positive integer is a factor of 72 if and only if the exponents in its prime factorization are less than or equal to the corresponding exponents in the prime factorization of 72.  Also, a positive integer is a perfect cube if and only if every exponent is a multiple of 3.  Therefore, in forming a perfect cube factor of 72, we have 2 choices for the exponent of $2$ (either 0 or 3) and only 1 choice for the exponent of 3 (namely 0).  There are $2\\cdot 1=\\boxed{2}$ ways to make these choices.
Action: Finish[\\boxed{2}]""",


    "Level 3": """Question: What is the least positive multiple of 25 for which the product of its digits is also a positive multiple of 25?
Thought: Every multiple of 25 ends in 00, 25, 50, or 75.  Since we want the product of the digits to be a positive multiple of 25, the final two digits must be either 25 or 75.\n\nA nonzero product of digits is a multiple of 25 exactly when two or more of the digits is are equal to 5. If a number ends in 75 and the product of its digits is a multiple of 25, then replacing 75 by 25 in that number will also give a smaller number whose product of digits is a multiple of 25.  Therefore we are looking for a number whose final two digits are 25 and for which 5 is one of the other digits.\n\nSince 525 is the smallest such number, the answer must be $\\boxed{525}$.
Action: Finish[\\boxed{525}]


Question: What is the smallest positive value of $x$ such that $x + 5678$ results in a palindrome?
Thought: We are asked to find the smallest palindrome greater than 5678 and subtract 5678 from it. The only palindrome in the 5600s is 5665, which is not greater than 5678.  The only palindrome in the 5700s is 5775, which is greater than 5678.  Therefore, 5775 is the smallest palindrome greater than 5678 and $x=5775-5678=\\boxed{97}$.
Action: Finish[\\boxed{97}]


Question: Convert $199_{10}$ to base 2. Let $x$ be the number of zeros and $y$ be the number of ones in base 2. What is the value of $y-x?$
Thought: The largest power of 2 that divides $199$ is $2^7$, which equals 128. Since $(1\\cdot 2^7)=128<199<(2\\cdot 2^7)=256$, the digit in the $2^7$ place is $1$. We know that $199-128=71$, and that $71$ can be expressed as $64+4+2+1$, or $(1\\cdot 2^6)+(1\\cdot 2^2)+(1\\cdot 2^1)+(1\\cdot 2^0)$. This means that $199_{10}=11000111_2$. Therefore, $x=3$ and $y=5$; and $y-x=5-3=\\boxed{2}$.
Action: Finish[\\boxed{2}]


Question: Let $x$ be a positive integer such that $9x\\equiv 1\\pmod{25}$.\n\nWhat is the remainder when $11+x$ is divided by $25$?
Thought: The given information can be expressed by writing $x\\equiv 9^{-1}\\pmod{25}$. Thus we wish to compute $11+9^{-1}\\pmod{25}$.\n\nModulo $25$, we can write $11$ as $11\\cdot (9\\cdot 9^{-1}) \\equiv (11\\cdot 9)\\cdot 9^{-1} \\equiv 99\\cdot 9^{-1}$. Thus \\begin{align*}\n11 + 9^{-1} &\\equiv 99\\cdot 9^{-1} + 1\\cdot 9^{-1} \\\\\n&\\equiv 100\\cdot 9^{-1} \\\\\n&\\equiv 0\\cdot 9^{-1} \\\\\n&\\equiv 0\\pmod{25},\n\\end{align*}so the remainder when $11+x$ is divided by $25$ is $\\boxed{0}$.\n\nNotice that the trick we used here is analogous to using a common denominator to add fractions.
Action: Finish[\\boxed{0}]


Question: Divide the product of the first five positive composite integers by the product of the next five composite integers. Express your answer as a common fraction.
Thought: The first ten positive composite integers are 4, 6, 8, 9, 10, 12, 14, 15, 16, 18. The desired quotient is $\\frac{4\\cdot6\\cdot8\\cdot9\\cdot10}{12\\cdot14\\cdot15\\cdot16\\cdot18}$. After cancellation, we get $\\frac{1}{14\\cdot3}=\\boxed{\\frac{1}{42}}$.
Action: Finish[\\boxed{\\frac{1}{42}}]""",

    "Level 4": """Question: How many ways can 1995 be factored as a product of two two-digit numbers? (Two factorizations of the form $a\\cdot b$ and $b\\cdot a$ are considered the same).
Thought: $1995=5\\cdot399=3\\cdot5\\cdot133=3\\cdot5\\cdot7\\cdot19$. Since $3\\cdot5\\cdot7=105$ has three digits, in any expression of $1995$ as the product of two two-digit numbers, $19$ must be a proper factor of one of them. $19\\cdot3=57$ and $19\\cdot5=95$ are two-digit numbers that are divisible by $19$ and divide $1995$, but $19\\cdot7=133$ and $19\\cdot3\\cdot5=285$ are three digits, so the only possible expressions of $1995$ as the product of two two-digit numbers are $57\\cdot35$ and $95\\cdot21$. So, there are $\\boxed{2}$ such factorizations.
Action: Finish[\\boxed{2}]


Question: To express 20 as a sum of distinct powers of 2, we would write $20 = 2^4 + 2^2$. The sum of the exponents of these powers is $4 + 2 = 6$. If 1562 were expressed as a sum of distinct powers of 2, what would be the least possible sum of the exponents of these powers?
Thought: By the uniqueness of the binary representation of positive integers, there is only one way to represent 1562 as a sum of distinct powers of $2$.  To find this representation, we convert 1562 to binary form.  The largest power of $2$ less than 1562 is $2^{10}=1024$.  The difference between 1024 and 1562 is $538$. The largest power of 2 less than 538 is $2^9=512$.  The difference between 538 and 512 is 26.  The largest power of 2 less than 26 is $2^4=16$, which leaves us with $26-16=10$. Continuing the process, we get $2^3=8$ and $2^1=2$. So, we have found that $1562=2^{10}+2^9+2^4+2^3+2^1$.  The sum of the exponents of 2 in this representation is $\\boxed{27}$.
Action: Finish[\\boxed{27}]


Question: What is the product of the digits in the base 8 representation of $6543_{10}$?
Thought: To convert to base 8, we realize $8^{5}>6543_{10}>8^{4}$. So, we can tell that $6543_{10}$ in base eight will have five digits. $8^{4}=4096$, which can go into 6543 only one time at most, leaving $6543-1\\cdot4096 = 2447$ for the next four digits. $8^{3}=512$ goes into 2447 four times at most, leaving us with $2447-4\\cdot512 = 399$. Then, $8^{2}=64$ goes into 399 six times at most, leaving $399-6\\cdot64 = 15$. Next, we have $8^{1}=8$, which can go into 15 one time, leaving $15-1\\cdot8 = 7$ for the ones digit. All together, the base eight equivalent of $6543_{10}$ is $14617_{8}$.  We are looking for the product of the digits, which is $1\\cdot4\\cdot6\\cdot1\\cdot7 = \\boxed{168}$.
Action: Finish[\\boxed{168}]


Question: What is the smallest integer $b > 3$ for which the base $b$ number $23_b$ is a perfect square?
Thought: Since $23_b = 2b + 3$ and $b > 3$, $23_b$ can be any odd integer greater than $2(3) + 3 = 9$.  We are looking for the next smallest odd perfect square, which is $5^2 = 25$.  Since $2b + 3 = 25$, $b = \\boxed{11}$ is our answer.
Action: Finish[\\boxed{11}]


Question: The product of the positive integer divisors of a positive integer $n$ is 729. Find $n$.
Thought: Suppose that $n$ has $d$ divisors and that $d$ is even. Since the divisors come in pairs whose product is $n$, the product of the divisors of $n$ is $n^{d/2}$. For example, if $n=12$ then the product of the divisors is $(1\\cdot 12)(2\\cdot 6)(3\\cdot 4)=12^3$. If $d$ is odd, then there are $(d-1)/2$ pairs which give a product of $n$, as well as the divisor $\\sqrt{n}$. So again the product of the divisors is $n^{(d-1)/2}n^{1/2}=n^{d/2}$. For example, if $n=16$, then the product of the divisors of $n$ is $(1\\cdot 16)(2\\cdot 8)(4)=16^{5/2}$. To summarize, we have found that the product of the positive integers divisors of a positive integer $n$ is $n^{d/2}$, where $d$ is the number of divisors of $n$. Writing 729 as $3^6$, then, we have $n^{d/2}=3^6$, which implies $n^d=3^{12}$. So the possible values of $(n,d)$ are $(3,12)$, $(9,6)$, $(27,4)$, $(81,3)$ and $(729,2)$. We find that only in the third case $(n,d)=(27,4)$ is $d$ the number of divisors of $n$, so $n=\\boxed{27}$.
Action: Finish[\\boxed{27}]""",

    "Level 5": """Question: When the greatest common divisor and least common multiple of two integers are multiplied, their product is 200. How many different values could be the greatest common divisor of the two integers?
Thought: We know that $\\gcd(a,b) \\cdot \\mathop{\\text{lcm}}[a,b] = ab$ for all positive integers $a$ and $b$.  Hence, in this case, $ab = 200$.  The prime factorization of 200 is $2^3 \\cdot 5^2$, so $a = 2^p \\cdot 5^q$ and $b = 2^r \\cdot 5^s$ for some nonnegative integers $p$, $q$, $r$, and $s$.  Then $ab = 2^{p + r} \\cdot 5^{q + s}$.  But $ab = 200 = 2^3 \\cdot 5^2$, so $p + r = 3$ and $q + s = 2$.\n\nWe know that $\\gcd(a,b) = 2^{\\min\\{p,r\\}} \\cdot 5^{\\min\\{q,s\\}}$.  The possible pairs $(p,r)$ are $(0,3)$, $(1,2)$, $(2,1)$, and $(3,0)$, so the possible values of $\\min\\{p,r\\}$ are 0 and 1.  The possible pairs $(q,s)$ are $(0,2)$, $(1,1)$, and $(2,0)$, so the possible values of $\\min\\{q,s\\}$ are 0 and 1.\n\nTherefore, the possible values of $\\gcd(a,b)$ are $2^0 \\cdot 5^0 = 1$, $2^1 \\cdot 5^0 = 2$, $2^0 \\cdot 5^1 = 5$, and $2^1 \\cdot 5^1 = 10$, for a total of $\\boxed{4}$ possible values.
Action: Finish[\\boxed{4}]


Question: Two numbers $90$ and $m$ share exactly three positive divisors. What is the greatest of these three common divisors?
Thought: Recall that the common divisors of two integers are precisely the divisors of the greatest common divisor. So, for two numbers to have exactly three positive divisors in common, those divisors must be $1$, $p$, and $p^2$ such that $p$ is prime. We now look at the prime factorization of $90$: $90=2 \\cdot 3^2 \\cdot 5$. Since $3^2$ is the only perfect square divisor of $90$, the divisors that $90$ and $m$ share must be $1$, $3$, and $9$. The largest of these three numbers is $\\boxed{9}$.
Action: Finish[\\boxed{9}]


Question: Two circles, one of radius 5 inches, the other of radius 2 inches, are tangent at point P. Two bugs start crawling at the same time from point P, one crawling along the larger circle at $3\\pi$ inches per minute, the other crawling along the smaller circle at $2.5\\pi$ inches per minute. How many minutes is it before their next meeting at point P?
Thought: The circumference of the larger circle, $C_1$, is $2\\cdot5\\pi=10\\pi$. The circumference of the smaller circle, $C_2$, is $2\\cdot2\\pi=4\\pi$. The bug on $C_1$ crawls the circumference in $\\frac{10\\pi}{3\\pi}=\\frac{10}{3}$ minutes, while the bug on $C_2$ crawls the circumference in $\\frac{4\\pi}{2.5\\pi}=\\frac{8}{5}$ minutes. The two bugs will meet at point P in some $t$ minutes, when $t\\div\\frac{10}{3}=\\frac{3t}{10}$ and $t\\div\\frac{8}{5}=\\frac{5t}{8}$ are both integers. We have $\\text{GCD}(3,10)=\\text{GCD}(5,8)=1$, so we have to find the LCM of $10=2\\cdot5$ and $8=2^3$. The LCM is $2^3\\cdot5=40$, so the bugs will next meet in $t=\\boxed{40}$ minutes.
Action: Finish[\\boxed{40}]


Question: Billy and Bobbi each selected a positive integer less than 200. Billy's number is a multiple of 18, and Bobbi's number is a multiple of 24. What is the probability that they selected the same number? Express your answer as a common fraction.
Thought: We must first find how many positive integers less than 200 are multiples of both 18 and 24. $18=2\\cdot3^2$ and $24=2^3\\cdot3$, so the LCM of 18 and 24 is $2^3\\cdot3^2=72$. Therefore, an integer is a multiple of both 18 and 24 if and only if it is a multiple of 72.\n\nDividing 200 by 72 gives quotient 2 (and remainder 56), so there are 2 multiples of 72 less than 200.\n\nDividing 200 by 18 gives quotient 11 (and remainder 2), so there are 11 multiples of 18 less than 200.\n\nDividing 200 by 24 gives quotient 8 (and remainder 8), so there are 8 multiples of 24 less than 200.\n\nTherefore, Billy and Bobbi together can pick $11\\cdot8=88$ different two-number combinations, and 2 of these involve them choosing the same number (the two multiples of 72 are the possible duplicate numbers). Thus, the probability that they selected the same number is $2/88=\\boxed{\\frac{1}{44}}$.
Action: Finish[\\boxed{\\frac{1}{44}}]


Question: What is the sum of all integer values of $n$ such that $\\frac{20}{2n - 1}$ is an integer?
Thought: The expression $2n-1$ is odd for every integer $n$, and conversely every odd integer takes the form $2n-1$ for some integer $n$.  Therefore, there is one solution $n$ for each (not necessarily positive) odd divisor of 20.  The positive odd divisors of 20 are 1 and 5, so we solve $2n-1=-5$, $2n-1=-1$, $2n-1=1$, and $2n-1=5$ to find the solutions $n=-2$, $n=0$, $n=1$, and $n=3$.  These values for $n$ sum to $\\boxed{2}$.
Action: Finish[\\boxed{2}]"""
}