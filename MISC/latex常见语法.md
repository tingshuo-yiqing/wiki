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

## 计算几和

### 1. 向量与点 (Vectors and Points)

| 描述      | 显示效果                     | LaTeX 代码                       | 备注                         |
| :-------- | :--------------------------- | :------------------------------- | :--------------------------- |
| 小写向量  | $\vec{a}, \vec{v}$           | `\vec{a}, \vec{v}`               | 简单的向量                   |
| 粗体向量  | $\mathbf{v}, \boldsymbol{v}$ | `\mathbf{v}` 或 `\boldsymbol{v}` | 常用表示物理或几何向量       |
| 有向线段  | $\overrightarrow{AB}$        | `\overrightarrow{AB}`            | 强调起点和终点               |
| 点坐标    | $(x, y)$                     | `(x, y)`                         |                              |
| 点列/下标 | $P_1, P_2, \dots, P_n$       | `P_1, P_2, \dots, P_n`           | 注意 `\dots`                 |
| 二维空间  | $\mathbb{R}^2$               | `\mathbb{R}^2`                   | 需要 `amsfonts` 或 `amssymb` |

### 2. 向量运算 (Vector Operations)

| 描述                 | 显示效果                                                     | LaTeX 代码                                       | 备注               |
| :------------------- | :----------------------------------------------------------- | :----------------------------------------------- | :----------------- |
| 点积 (Dot Product)   | $a \cdot b$ 或 $\langle a, b \rangle$                        | `a \cdot b` 或 `\langle a, b \rangle`            | 不要用 `.`         |
| 叉积 (Cross Product) | $a \times b$                                                 | `a \times b`                                     | 常用表示二维伪叉积 |
| 模长 (Norm/Length)   | $\|v\|$ 或 $|v|$                                             | `\|v\|` 或 `|v|`                                 | 推荐 `\|`          |
| 距离                 | $\operatorname{dist}(A, B)$                                  | `\operatorname{dist}(A, B)`                      | 定义操作符         |
| 行列式               | $\det(M)$ 或 $\begin{vmatrix} x_1 & y_1 \\ x_2 & y_2 \end{vmatrix}$ | `\det(M)` 或 `\begin{vmatrix} ... \end{vmatrix}` | 叉积的行列式形式   |

### 4. 集合与凸包 (Sets & Convex Hull)

| 描述 | 显示效果                                    | LaTeX 代码              | 备注         |
| :--- | :------------------------------------------ | :---------------------- | :----------- |
| 凸包 | $\operatorname{CH}(S)$ 或 $\mathcal{CH}(S)$ | `\operatorname{CH}(S)`  | Convex Hull  |
| 边界 | $\partial P$                                | `\partial P`            | 多边形的边界 |
| 内部 | $\operatorname{int}(P)$                     | `\operatorname{int}(P)` | Interior     |
| 交集 | $A \cap B$                                  | `A \cap B`              |              |
| 并集 | $A \cup B$                                  | `A \cup B`              |              |
| 属于 | $p \in S$                                   | `p \in S`               |              |
| 包含 | $S \subseteq T$                             | `S \subseteq T`         |              |

### 5. 常用几何关系与逻辑 (Relations & Logic)

| 描述       | 显示效果                            | LaTeX 代码         | 备注         |
| :--------- | :---------------------------------- | :----------------- | :----------- |
| 相似       | $\triangle ABC \sim \triangle DEF$  | `\sim`             |              |
| 全等       | $\triangle ABC \cong \triangle DEF$ | `\cong`            |              |
| 大约等于   | $a \approx b$                       | `\approx`          |              |
| 恒等于     | $a \equiv b$                        | `\equiv`           |              |
| 推出       | $\implies$                          | `\implies`         |              |
| 渐进复杂度 | $O(N \log N)$                       | `O(N \log N)`      | 简单的写法   |
| 花体复杂度 | $\mathcal{O}(N^2)$                  | `\mathcal{O}(N^2)` | 更正式的写法 |

## 希腊字母

### 1. 小写希腊字母 (Lowercase)

|    字母    | LaTeX 语法 |    字母    | LaTeX 语法            |
| :--------: | :--------- | :--------: | :-------------------- |
|  $\alpha$  | `\alpha`   |   $\nu$    | `\nu`                 |
|  $\beta$   | `\beta`    |   $\xi$    | `\xi`                 |
|  $\gamma$  | `\gamma`   |    $o$     | `o` (与英文字母o相同) |
|  $\delta$  | `\delta`   |   $\pi$    | `\pi`                 |
| $\epsilon$ | `\epsilon` |   $\rho$   | `\rho`                |
|  $\zeta$   | `\zeta`    |  $\sigma$  | `\sigma`              |
|   $\eta$   | `\eta`     |   $\tau$   | `\tau`                |
|  $\theta$  | `\theta`   | $\upsilon$ | `\upsilon`            |
|  $\iota$   | `\iota`    |   $\phi$   | `\phi`                |
|  $\kappa$  | `\kappa`   |   $\chi$   | `\chi`                |
| $\lambda$  | `\lambda`  |   $\psi$   | `\psi`                |
|   $\mu$    | `\mu`      |  $\omega$  | `\omega$              |

---

### 2. 大写希腊字母 (Uppercase)

**注意：** 许多大写希腊字母与拉丁字母（英文字母）字形相同（如 A, B, E, Z），因此 LaTeX 没有专门的命令，直接输入对应的英文字母即可。

|   字母    | LaTeX 语法 |    字母    | LaTeX 语法 |
| :-------: | :--------- | :--------: | :--------- |
|    $A$    | `A`        |    $N$     | `N`        |
|    $B$    | `B`        |   $\Xi$    | `\Xi`      |
| $\Gamma$  | `\Gamma`   |    $O$     | `O`        |
| $\Delta$  | `\Delta`   |   $\Pi$    | `\Pi`      |
|    $E$    | `E`        |    $P$     | `P`        |
|    $Z$    | `Z`        |  $\Sigma$  | `\Sigma`   |
|    $H$    | `H`        |    $T$     | `T`        |
| $\Theta$  | `\Theta`   | $\Upsilon$ | `\Upsilon` |
|    $I$    | `I`        |   $\Phi$   | `\Phi`     |
|    $K$    | `K`        |    $X$     | `X`        |
| $\Lambda$ | `\Lambda`  |   $\Psi$   | `\Psi`     |
|    $M$    | `M`        |  $\Omega$  | `\Omega`   |

---

### 3. 变体形式 (Variants)

数学中经常会用到同一字母的不同写法，LaTeX 提供了相应的 `var` 前缀命令：

|  标准形式  | 语法       |   变体形式    | 语法          |
| :--------: | :--------- | :-----------: | :------------ |
| $\epsilon$ | `\epsilon` | $\varepsilon$ | `\varepsilon` |
|  $\theta$  | `\theta`   |  $\vartheta$  | `\vartheta`   |
|   $\rho$   | `\rho`     |   $\varrho$   | `\varrho`     |
|  $\sigma$  | `\sigma`   |  $\varsigma$  | `\varsigma`   |
|   $\phi$   | `\phi`     |   $\varphi$   | `\varphi$     |
|   $\pi$    | `\pi`      |   $\varpi$    | `\varpi$      |

## 三角函数

### 1. 基础角度符号
*   **角度符号**: `\angle` $\to \angle$ (如：$\angle ABC$)
*   **度数 ($^\circ$)**:
    *   常用：`^\circ` $\to ^\circ$ (如：`90^\circ`)
        *   更专业（需 `gensymb` 宏包）：`\degree` $\to \degree$
    *   带单位（需 `siunitx` 宏包，推荐）：`\ang{45}` $\to 45^\circ$
*   **弧度 (Rad)**: 通常直接写 $\pi$ (`\pi`)。

### 2. 三角函数
LaTeX 预定义了标准三角函数，**必须使用反斜杠**，否则字母会变成倾斜的变量名：

*   **基本函数**: `\sin`, `\cos`, `\tan` $\to \sin, \cos, \tan$
*   **余函数**: `\cot`, `\sec`, `\csc` $\to \cot, \sec, \csc$
*   **反三角函数**: `\arcsin`, `\arccos`, `\arctan` $\to \arcsin, \arccos, \arctan$
*   **Atan2 (自定义算子)**:
    由于 LaTeX 默认没有 `\atan2`，通常建议使用 `\operatorname`：
    `\operatorname{atan2}(y, x)` $\to \operatorname{atan2}(y, x)$

### 3. 几何图形描述
*   **垂直**: `\perp` $\to \perp$ (如：$AB \perp CD$)
*   **平行**: `\parallel` $\to \parallel$ (如：$AB \parallel CD$)
*   **相似**: `\sim` $\to \sim$
*   **全等**: `\cong` $\to \cong$
*   **三角形**: `\triangle` $\to \triangle$ (如：$\triangle ABC$)
*   **射线/向量**: 
    *   `\vec{a}` $\to \vec{a}$
    *   `\overrightarrow{AB}` $\to \overrightarrow{AB}$

### 4. 希腊字母 (常用于表示角)
*   `\theta` $\to \theta$ (最常用)
*   `\alpha, \beta, \gamma` $\to \alpha, \beta, \gamma$
*   `\phi, \varphi` $\to \phi, \varphi$
*   `\omega` $\to \omega$

### 5. 分、秒 (角度单位)
在表示 $30^\circ 15' 20''$ 时：
*   **分**: `'` (单引号) $\to '$
*   **秒**: `''` (双单引号) 或 `^{\prime\prime}` $\to ''$
*   **示例**: `$30^\circ 15' 20''$` $\to 30^\circ 15' 20''$


