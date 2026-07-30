library(tidyverse)

# Read data
data <- read_csv("synthetic_applicants.csv")

# Convert categorical variables to factors
data <- data %>%
  mutate(
    smoker = factor(smoker),
    bmi_category = factor(bmi_category),
    occupation_risk = factor(occupation_risk),
    health_risk = factor(health_risk)
  )

# Baseline: Linear regression
linear_model <- lm(
  annual_premium ~ age + smoker + coverage + term_years,
  data = data
)
summary(linear_model)

# Gamma GLM (more appropriate since premium is positive and right-skewed)
gamma_model <- glm(
  annual_premium ~ age + smoker + coverage + term_years,
  family = Gamma(link = "log"),
  data = data
)
summary(gamma_model)

# Compare model performance
data$pred_linear <- predict(linear_model, data)
data$pred_gamma <- predict(gamma_model, data, type = "response")

mae_linear <- mean(abs(data$annual_premium - data$pred_linear))
mae_gamma <- mean(abs(data$annual_premium - data$pred_gamma))

rmse_linear <- sqrt(mean((data$annual_premium - data$pred_linear)^2))
rmse_gamma <- sqrt(mean((data$annual_premium - data$pred_gamma)^2))

cat("Linear Model - MAE:", round(mae_linear, 2), " RMSE:", round(rmse_linear, 2), "\n")
cat("Gamma GLM    - MAE:", round(mae_gamma, 2), " RMSE:", round(rmse_gamma, 2), "\n")