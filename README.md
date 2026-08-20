<div align="center">

# 🗃️ SQL Practice — LeetCode Top 50

**Structured solutions to the LeetCode SQL 50 study plan, built while prepping for Data/Business Analyst interviews.**

![LeetCode](https://img.shields.io/badge/LeetCode-SQL%2050-FFA116?style=flat&logo=leetcode&logoColor=white)
![Progress](https://img.shields.io/badge/Progress-50%2F50-brightgreen?style=flat)
![SQL](https://img.shields.io/badge/SQL-MySQL%20%7C%20PostgreSQL-4479A1?style=flat&logo=postgresql&logoColor=white)
![Last Commit](https://img.shields.io/github/last-commit/YOUR_USERNAME/YOUR_REPO?style=flat)

</div>

---

## 📌 About

This repo tracks my solutions to the **[LeetCode SQL 50](https://leetcode.com/studyplan/top-sql-50/)** study plan — synced automatically via the LeetCode–GitHub integration. It's part of my prep for Analyst interviews (SQL rounds, live query problems, and root-cause style questions).

Every solution includes:
- ✅ The problem statement (linked)
- ✅ My query with inline comments explaining the logic
- ✅ Time complexity / approach notes where relevant
- ✅ Key SQL concept(s) practiced

---

## 📊 Progress

| Difficulty | Solved | Total |
|---|---|---|
| 🟢 Easy | XX | 20 |
| 🟡 Medium | XX | 22 |
| 🔴 Hard | XX | 8 |
| **Total** | **XX** | **50** |

> Update these numbers as you go — or swap in a live stats card like [leetcode-stats-card](https://github.com/Amanrathi-Git/SQL_50_Leetcode/tree/main):
> `![LeetCode Stats](https://leetcode.com/u/aman_rathi_2310/)

---

## 🗂️ Problems by Concept

### Basic Queries & Filtering
| # | Problem | Difficulty | Concept |
|---|---|---|---|
| 1 | [Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products/) | Easy | WHERE, basic filtering |
| 2 | [Find Customer Referee](https://leetcode.com/problems/find-customer-referee/) | Easy | NULL handling |
| 3 | [Big Countries](https://leetcode.com/problems/big-countries/) | Easy | OR conditions |

### Joins
| # | Problem | Difficulty | Concept |
|---|---|---|---|
| 4 | [Employees Earning More Than Their Managers](https://leetcode.com/problems/employees-earning-more-than-their-managers/) | Easy | Self-join |
| 5 | [Combine Two Tables](https://leetcode.com/problems/combine-two-tables/) | Easy | LEFT JOIN |
| 6 | [Customer Who Visited but Did Not Make Any Transactions](https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/) | Easy | LEFT JOIN + NULL filter |

### Aggregation & Grouping
| # | Problem | Difficulty | Concept |
|---|---|---|---|
| 7 | [Group Sold Products By The Date](https://leetcode.com/problems/group-sold-products-by-the-date/) | Easy | GROUP_CONCAT / STRING_AGG |
| 8 | [Daily Leads and Partners](https://leetcode.com/problems/daily-leads-and-partners/) | Easy | GROUP BY, COUNT DISTINCT |
| 9 | [Classes More Than 5 Students](https://leetcode.com/problems/classes-more-than-5-students/) | Easy | HAVING |

### Subqueries & CTEs
| # | Problem | Difficulty | Concept |
|---|---|---|---|
| 10 | [Employees Whose Manager Left the Company](https://leetcode.com/problems/employees-whose-manager-left-the-company/) | Easy | Subquery |
| 11 | [Exchange Seats](https://leetcode.com/problems/exchange-seats/) | Medium | CASE + CTE |
| 12 | [Investments in 2016](https://leetcode.com/problems/investments-in-2016/) | Medium | Correlated subquery |

### Window Functions (interview favorite — companies test this hardest)
| # | Problem | Difficulty | Concept |
|---|---|---|---|
| 13 | [Rank Scores](https://leetcode.com/problems/rank-scores/) | Medium | RANK / DENSE_RANK |
| 14 | [Department Top Three Salaries](https://leetcode.com/problems/department-top-three-salaries/) | Hard | DENSE_RANK, PARTITION BY |
| 15 | [Nth Highest Salary](https://leetcode.com/problems/nth-highest-salary/) | Medium | OFFSET / LIMIT / window fn |

### String / Date Functions
| # | Problem | Difficulty | Concept |
|---|---|---|---|
| 16 | [Fix Names in a Table](https://leetcode.com/problems/fix-names-in-a-table/) | Easy | CONCAT, UPPER/LOWER |
| 17 | [Second Highest Salary](https://leetcode.com/problems/second-highest-salary/) | Medium | IFNULL, LIMIT/OFFSET |

---

## 🧠 Key Concepts Practiced

`JOINS` `WINDOW FUNCTIONS` `CTEs` `SUBQUERIES` `AGGREGATION` `GROUP BY / HAVING` `DATE FUNCTIONS` `STRING FUNCTIONS` `NULL HANDLING` `RANK / DENSE_RANK / ROW_NUMBER`

---


Each `.sql` file follows this format:

```sql
-- Problem: [Problem Name]
-- Difficulty: Medium
-- Concept: Window Functions (RANK)
-- Link: https://leetcode.com/problems/...

-- Approach: 
-- Rank scores in descending order, skipping ranks for ties (DENSE_RANK behavior)

SELECT score,
       DENSE_RANK() OVER (ORDER BY score DESC) AS 'rank'
FROM Scores;
```

---

## 🛠️ Tech

- SQL dialect: MySQL / PostgreSQL (as required per problem)
- Auto-synced via [LeetCode's GitHub integration](https://leetcode.com/) on every accepted submission

---

## 🎯 Why This Repo Exists

Built while preparing for Data/Business Analyst interviews — SQL is consistently the first and heaviest-weighted technical round at most analyst roles. This repo doubles as a public log of consistent practice and a quick-reference cheat sheet for interview day.

---

## 📫 Connect

- LeetCode: [your-profile](https://leetcode.com/u/aman_rathi_2310/)

