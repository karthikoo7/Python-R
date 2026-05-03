# ============================
# BASIC GRAPHS IN R - DEMO
# ============================

# Clear the workspace
rm(list = ls())

# ----------------------------
# 1. SCATTER PLOT
# ----------------------------
x <- c(1, 2, 3, 4, 5)
y <- c(2, 4, 6, 8, 10)
plot(x, y,
     type = "p",                # 'p' = points
     main = "Scatter Plot",
     xlab = "X Values",
     ylab = "Y Values",
     col = "blue",
     pch = 5)          #Point shape        # solid circles

# ----------------------------
# 2. LINE GRAPH
# ----------------------------
plot(x, y,
     type = "l",                # 'l' = lines
     main = "Line Graph",
     xlab = "X",
     ylab = "Y",
     col = "red",
     lwd = 4)                   # line width

# ----------------------------
# 3. BAR CHART
# ----------------------------
fruits <- c("Apple", "Banana", "Mango", "Grapes")
counts <- c(20, 15, 30, 10)
barplot(counts,
        names.arg = fruits,
        col = "orange",
        main = "Fruit Counts",
        xlab = "Fruit",
        ylab = "Count")

# ----------------------------
# 4. PIE CHART
# ----------------------------
slices <- c(20, 15, 30, 10)
labels <- c("Apple", "Banana", "Mango", "Grapes")
pie(slices,
    labels = labels,
    main = "Fruit Distribution",
    col = rainbow(length(slices)))

# ----------------------------
# 5. HISTOGRAM
# ----------------------------
data <- c(1, 2, 2, 3, 3, 3, 4, 5, 5, 6)
hist(data,
     main = "Histogram Example",
     xlab = "Values",
     ylab = "Frequency",
     col = "lightblue",
     border = "black")

# ----------------------------
# 6. BOXPLOT
# ----------------------------
values <- c(10, 20, 15, 25, 30, 35, 40)
boxplot(values,
        main = "Boxplot Example",
        ylab = "Values",
        col = "lightgreen",
        border = "darkgreen")

# ----------------------------
# END OF SCRIPT
# ----------------------------
