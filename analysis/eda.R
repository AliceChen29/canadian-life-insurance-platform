library(tidyverse)

# Read the synthetic data
data <- read_csv("synthetic_applicants.csv")

# Quick look at the data
glimpse(data)
summary(data)

# Distribution of age
ggplot(data, aes(x = age)) +
  geom_histogram(binwidth = 5, fill = "steelblue", color = "white") +
  labs(title = "Age Distribution of Applicants", x = "Age", y = "Count")

# Distribution of annual premium
ggplot(data, aes(x = annual_premium)) +
  geom_histogram(bins = 40, fill = "darkorange", color = "white") +
  labs(title = "Distribution of Estimated Annual Premium", x = "Annual Premium ($)", y = "Count")

# Premium by smoking status
ggplot(data, aes(x = factor(smoker), y = annual_premium)) +
  geom_boxplot(fill = "lightgreen") +
  labs(title = "Premium by Smoking Status", x = "Smoker (0 = No, 1 = Yes)", y = "Annual Premium ($)")

# Premium vs age, colored by smoking status
ggplot(data, aes(x = age, y = annual_premium, color = factor(smoker))) +
  geom_point(alpha = 0.4) +
  labs(title = "Premium vs Age by Smoking Status", x = "Age", y = "Annual Premium ($)", color = "Smoker")
