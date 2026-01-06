## 同余

### 1. 核心符号：同余与取模

这是最基础的表达方式，区分**作为运算符**（如 $a \% b$）和**作为同余式**（如 $a \equiv b$）。

| 效果                 | LaTeX 语法           | 说明                           |
| :------------------- | :------------------- | :----------------------------- |
| $a \equiv b$         | `a \equiv b`         | 同余符号（三横线）             |
| $a \equiv b \pmod m$ | `a \equiv b \pmod m` | **最常用**。自动添加括号和间距 |
| $a \equiv b \pod m$  | `a \equiv b \pod m`  | 省略 "mod" 字样，只留括号      |
| $x = a \bmod m$      | `x = a \bmod m`      | 作为二元运算符（间距较紧凑）   |
| $a \not\equiv b$     | `a \not\equiv b`     | 不通余                         |

---

### 2. 幂运算与逆元（费马小定理/欧拉定理）

在处理逆元时，经常需要写指数。

| 效果                              | LaTeX 语法                        |
| :-------------------------------- | :-------------------------------- |
| $a^{p-2} \pmod p$                 | `a^{p-2} \pmod p$                 |
| $a \cdot a^{-1} \equiv 1 \pmod m$ | `a \cdot a^{-1} \equiv 1 \pmod m` |
| $x \equiv a^b \pmod n$            | `x \equiv a^b \pmod n`            |

---

### 3. 整除相关（数论基础）

在讨论约数、倍数或莫比乌斯反演时经常用到。 

| 效果             | LaTeX 语法       | 说明           |
| :--------------- | :--------------- | :------------- |
| $d \mid n$       | `d \mid n`       | $d$ 整除 $n$   |
| $d \nmid n$      | `d \nmid n`      | $d$ 不整除 $n$ |
| $\gcd(a, b) = 1$ | `\gcd(a, b) = 1` | 最大公约数     |
| $\sum_{i=1}^n$   | `\sum_{i=1}^n`   | 求和符号       |

---

### 4. 同余方程组（中国剩余定理 CRT）

当你需要展示多个方程构成的方程组时，使用 `cases` 环境：

**效果：**
$$
\begin{cases}
x \equiv a_1 \pmod{m_1} \\
x \equiv a_2 \pmod{m_2}
\end{cases}
$$

**代码：**
```latex
\begin{cases}
x \equiv a_1 \pmod{m_1} \\
x \equiv a_2 \pmod{m_2}
\end{cases}
```

---

### 5. 分式表示（组合数取模/逆元）

虽然在同余式中很少直接写除法，但在推导过程中常用 `\frac`：

*   **语法：** `\frac{分子}{分母}`
*   **例子：** $x \equiv \frac{a}{b} \pmod p$ 写法为 `x \equiv \frac{a}{b} \pmod p`。
*   **技巧：** 如果在行间（inline）嫌分式太小，可以用 `\dfrac`。

