## [Monte Carlo simulation](https://github.com/gabriellegall/Python_Portfolio/blob/main/Monte-Carlo-simulation/monte_carlo_simulation.py)

**Context** : in the M&A case study ["Printicomm's Proposed Acquisition of Digitech: Negotiating Price and Form of Payment"](https://store.hbr.org/product/printicomm-s-proposed-acquisition-of-digitech-negotiating-price-and-form-of-payment/UV0087), company sellers are offered earnout contracts which payoff depends on the operating income generated by the company in the next few years. Those contracts can be valued like a call option under some assumptions of growth and operating margin.

**Script** : this script runs a Monte Carlo simulation to estimate the value of those earnout contracts under different scenarios of financial performance.

![illustration](https://github.com/gabriellegall/Python_Portfolio/blob/main/images/image7.PNG?raw=true)

## [Hypergeometric success probabilities](https://github.com/gabriellegall/Python_Portfolio/blob/main/Hypergeometric-success-probabilities/hypergeometric%20_success_probabilities_v1.py)

**Context** : one of my favorite board games is called [7 Wonders Duel](https://board-games-galore.fandom.com/wiki/7_Wonders:_Duel). It's a card based strategy game which involves some risk taking and gambling at the most decisive points. In those scenarios, some critical cards can get revealed among all the cards present on the board. In this context, we want to know the probability of obtaining at least 1,2,3 of those critical cards among all hidden cards if we get to play 1,2,3 times in a row. 

**Script** : this script calculates the probabilities of at least 1,2,3 sucess(es) across a probability tree with 1,2 and 3 branches for all scenarios of 'desired hidden cards' and 'hidden cards'. Below are the probabilities of at least 1 success if we get to play 1,2,3 times in a row for all scenarios.

![illustration](https://github.com/gabriellegall/Python_Portfolio/blob/main/images/image4.PNG?raw=true)

## [Central Limit Theorem](https://github.com/gabriellegall/Python_Portfolio/blob/main/Central-limit-theorem/central_limit_theorem.py)

**Context** : the central limit theorem (CLT) states that, given a sufficiently large sample size, the sampling distribution of the averages for a variable will approximate a normal distribution regardless of that variable’s distribution in the population. This theory is central to hypothesis testing since it enables researchers to know the hypothetical sampling distribution of averages for any random variable with finite mean and variance.

**Script** : this script shows the sampling distribution of 1000 averages for Bernoulli samples with various sizes. The script also contains results of a normality test (Jarque–Bera test) for each of those distributions.

![illustration](https://github.com/gabriellegall/Python_Portfolio/blob/main/images/image3.PNG?raw=true)

## [Law of Large Numbers](https://github.com/gabriellegall/Python_Portfolio/blob/main/Law-of-large-numbers/law_of_large_numbers_animated_v1.py)

**Context** : the law of large numbers (LLN) states that, as a sample size grows, its average gets closer to the population average. Another way to express this rule is that the absolute deviation from the population average tends towards zero as the sample size grows.

**Script** : this script calculates the sample average of a Bernoulli variable for various sample sizes and plots the results in a dynamic time series.

![illustration](https://github.com/gabriellegall/Python_Portfolio/blob/main/images/image2.GIF?raw=true)

## [A/B proportion testing](https://github.com/gabriellegall/Python_Portfolio/blob/main/AB-proportion-testing/ab_proportion_testing.py)

**Context** : the question of whether or not there is a significant difference between the mean response of two groups in an experiment can be solved by a z-test based on the central limit theorem. Specifically, the proportion of response in the two groups can be thought of as a Bernoulli random variable with a known mean sampling distribution. The theory behind the A/B proportion test is described in more detail in [my notes.](https://github.com/gabriellegall/Python_Portfolio/blob/main/documentation/ab_proportion_testing.pdf) The data and the use case was taken from [an article](https://towardsdatascience.com/the-math-behind-a-b-testing-with-example-code-part-1-of-2-7be752e1d06f) published on towardsdatascience in which the percent response to a webpage design is compared to a control group (two-sided test). 

**Script** : this script illustrates the scipy.stats.proportions_ztest function and breaks down the theory behind it to achieve the same results.

![illustration](https://github.com/gabriellegall/Python_Portfolio/blob/main/images/image8.PNG?raw=true)

## [Binomial testing](https://github.com/gabriellegall/Python_Portfolio/blob/main/Binomial-testing/binomial_testing.py)
**Context** : the binomial test is a simple but powerful statistical tool that I have used on some occasions to confront certain hypotheses to a statistical reality. It is an exact test of the statistical significance of deviations from a theoretically expected distribution of observations into two categories.

**Script** : this script illustrates the scipy.stats.binom_test function and breaks down the theory behind it to achieve the same results. [The example](https://github.com/gabriellegall/Python_Portfolio/blob/main/images/image6.PNG?raw=true) is taken from [the Wikipedia page](https://en.wikipedia.org/wiki/Binomial_test) on binomial testing. This example tests whether the number of "6" obtained from 251 dice rolls can help us determine if the dice is rigged to return this number more often (one-sided test).

![illustration](https://github.com/gabriellegall/Python_Portfolio/blob/main/images/image5.PNG?raw=true)

## [Simple linear regression](https://github.com/gabriellegall/Python_Portfolio/blob/main/Simple-linear-regressions/simple_linear_regressions.py)

**Context** : the capital asset pricing model (CAPM) describes the relationship between systematic risk (market risk) and expected returns for assets, particularly stocks. The regression coefficient Beta is therefore a metric to evaluate the risk compensation that investors should expect for investing in a specific company.

**Script** : this script computes the linear regression coefficient Beta for stock returns from 3 different companies. The choosen independent variable is the S&P 500 market return. In this example, the risk free rate is assumed to be zero. The monthly stock returns were taken from the [Regressit website.](https://regressit.com/data.html)

![illustration](https://github.com/gabriellegall/Python_Portfolio/blob/main/images/image1.PNG?raw=true)

## [Logistic regression](https://github.com/gabriellegall/Python_Portfolio/blob/main/Logistic-regression/logistic_regression.py)

**Context** : 

**Script** : 

![illustration](https://github.com/gabriellegall/Python_Portfolio/blob/main/images/image9.PNG?raw=true)

