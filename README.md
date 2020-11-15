## [Binomial success probabilities](https://github.com/gabriellegall/Python_Portfolio/blob/main/Binomial-success-probabilities/binomial-success-probabilities.py)
**Context** : one of my favorite board games is called [7 Wonders Duel](https://board-games-galore.fandom.com/wiki/7_Wonders:_Duel). It's a card based strategy game which involves some risk taking and gambling at the most decisive points. In those scenarios, some critical cards (called 'desired hidden cards' below) can get revealed among all the cards present on the board ('hidden cards'). Hence, we want to know the probability of obtaining one of those critical cards among all hidden cards if we get to play 1,2,3 times in a row. 

**Script** : this script calculates the probabilities of a sucess across a binomial tree with 1,2 and 3 branches for all scenarios of 'desired hidden cards' and 'hidden cards' (no replacement).

![illustration](https://github.com/gabriellegall/Python_Portfolio/blob/main/images/image4.PNG?raw=true)

## [Central Limit Theorem](https://github.com/gabriellegall/Python_Portfolio/blob/main/Central-limit-theorem/central_limit_theorem.py)

**Context** : the central limit theorem (CLT) states that, given a sufficiently large sample size, the sampling distribution of the averages for a variable will approximate a normal distribution regardless of that variable’s distribution in the population. The required sample size depends on how far the population distribution is from a normal distribution (typically researchers assume a sample size of 30).

**Script** : this script shows the sampling distribution of 1000 averages for Bernoulli samples with various sizes. The script also contains results of a normality test (Jarque–Bera test) for each of those distributions.

![illustration](https://github.com/gabriellegall/Python_Portfolio/blob/main/images/image3.PNG?raw=true)

## [Law of Large Numbers](https://github.com/gabriellegall/Python_Portfolio/blob/main/Law-of-large-numbers/law_of_large_numbers_animated.py)

**Context** : the law of large numbers (LLN) states that, as a sample size grows, its average gets closer to the population average. Another way to express this rule is that the absolute deviation from the population average tends towards zero as the sample size grows.

**Script** : this script calculates the sample average of a Bernoulli variable for various sample sizes and plots the results in a dynamic time series.

![illustration](https://github.com/gabriellegall/Python_Portfolio/blob/main/images/image2.GIF?raw=true)

## [Simple Linear Regression](https://github.com/gabriellegall/Python_Portfolio/blob/main/Simple-linear-regressions/simple_linear_regressions.py)

**Context** : the capital asset pricing model (CAPM) describes the relationship between systematic risk (market risk) and expected returns for assets, particularly stocks. The regression coefficient Beta is therefore a metric to evaluate the risk compensation that investors should expect for investing in a specific company.

**Script** : this script computes the linear regression coefficient Beta for stock returns from 3 different companies. The choosen independent variable is the S&P 500 market return. In this example, the risk free rate is assumed to be zero.

![illustration](https://github.com/gabriellegall/Python_Portfolio/blob/main/images/image1.PNG?raw=true)
