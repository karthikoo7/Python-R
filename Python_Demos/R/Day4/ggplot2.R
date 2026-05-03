# ----------------------------
# 1. Scatter Plot — Relationship Between Two Variables
# Goal: See how car weight (`wt`) affects mileage (`mpg`)
# ----------------------------

library(ggplot2)

ggplot(mtcars, aes(x = wt, y = mpg)) +
  geom_point(color = "blue", size = 3) +
  labs(
    title = "Scatter Plot: Car Weight vs Mileage",
    x = "Weight (1000 lbs)",
    y = "Miles per Gallon"
  ) +
  theme_minimal()
#📊 **Insight:** As car weight increases, fuel efficiency (mpg) tends to decrease — a negative correlation.




# ----------------------------
# 🔹 2. Line Plot — Trend Over Time
#Goal: Show how unemployment changes over time
# ----------------------------
ggplot(economics, aes(x = date, y = unemploy)) +
  geom_line(color = "darkgreen", linewidth = 1) +
  labs(
    title = "Unemployment Over Time",
    x = "Year",
    y = "Number of Unemployed"
  ) +
  theme_light()


#📊 **Insight:** Ideal for showing trends or time series data.




# ----------------------------
# 🔹 3. Bar Chart — Frequency of Categories
#*Goal:** Count number of cars by cylinder type
#*# ----------------------------

ggplot(mtcars, aes(x = factor(cyl))) +
  geom_bar(fill = "orange", color = "black") +
  labs(
    title = "Bar Chart: Count of Cars by Cylinders",
    x = "Cylinders",
    y = "Count"
  ) +
  theme_classic()

#📊 **Insight:** Most cars in `mtcars` have 4 or 8 cylinders.





# ----------------------------
# 🔹 4. Histogram — Distribution of a Variable
#Goal:** Understand the distribution of car mileage (`mpg`)
# ----------------------------
ggplot(mtcars, aes(x = mpg)) +
  geom_histogram(binwidth = 2, fill = "steelblue", color = "white") +
  labs(
    title = "Histogram: Distribution of Mileage",
    x = "Miles per Gallon",
    y = "Frequency"
  ) +
  theme_minimal()
#📊 **Insight:** You can see the most common mileage range for the cars.




# ----------------------------
# 🔹 5. Box Plot — Compare Distributions Across Categories
#Goal:** Compare highway mileage (`hwy`) across car classes
# ----------------------------

ggplot(mpg, aes(x = class, y = hwy)) +
  geom_boxplot(fill = "violet", color = "black") +
  labs(
    title = "Box Plot: Highway Mileage by Car Class",
    x = "Car Class",
    y = "Highway MPG"
  ) +
  theme_bw()
#📊 **Insight:** SUVs tend to have lower highway mileage; compact cars have higher.

