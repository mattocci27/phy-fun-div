# Trait-based ecology：追加スライド下書き

作成日：2026-10-28

元メモ：`/Users/mattocci/Obsidian/0-Inbox/trait授業方針.md`  
接続先：`phy-fun-div/main.qmd`（参照のみ・未変更）

既存スライドに合わせて本文は英語、講師メモは日本語。スライド本文は各節の箇条書き・表・式で、`::: notes`は発表者用。図は作図案であり、論文図の転載はまだ行っていない。実測でない数値は「授業用の仮想例」と明示した。

## 追加のねらいと挿入位置

中心となる問いを **“Which traits help predict which outcomes, through which processes?”** とする。既存の歴史・指標の説明は残し、「形質距離を計算する前に、予測対象と測定単位を選ぶ」という筋を補う。

| ブロック | 番号 | 既存スライドへの挿入候補 | 役割 |
|---|---|---|---|
| 予測対象と仮説 | 01–03 | `Plant functional traits` の直後、LESの前 | traitを測る理由と検証方法 |
| LESから植物全体へ | 04–06 | `Leaf Economic Spectrum (LES)` の直後 | サイズ・根・種子・水利用・防御 |
| 階層と群集要約 | 07–10 | 2枚目の `Rebuilding community ecology from functional traits` の後、convex hullの前 | 種平均と個体、CWMと多様性の区別 |
| パターンと過程 | 11 | `Community assembly and trait distribution` の直後 | 後のcompetitive hierarchyへの予告 |
| LMA分解と予測 | 12–14 | `Inter‑ and intra‑specific trait patterns often diverge` の直後 | 既存図からLMA分解への橋渡し |
| 共存への接続 | 15 | 既存のLMA分解スライドの直後 | 生理予測と共存予測を区別 |
| 発展事例 | 17–19 | 後半、まとめの前に選択して挿入 | 2026年の研究を問いと結び付ける |
| 振り返り | 16 | 発展事例を使う場合はその後、既存Summaryの前 | 学生が研究計画を言語化する |

基本案は01–16の16枚で、問いかけ込み約25–35分の追加を想定。時間が限られる場合は01・02・04・05・07・09・11・14の8枚を優先する。17–19は各2–3分の発展用で、すべて入れる必要はない。既存スライドとの重複は本稿末尾に整理した。

# スライド下書き：基礎と接続

<!-- Slide 01 | Plant functional traits の後 -->
## 01 | What do we want to predict?

| Outcome | Candidate information | Test |
|---|---|---|
| Distribution | Resource requirements, dispersal traits | Occurrence across environments |
| Growth and survival | Leaf, stem, and hydraulic traits | Repeated individual measurements |
| Coexistence | Resource use, competition, demography | Performance when rare |
| Ecosystem function | Traits, abundance, plant size | Productivity or nutrient fluxes |

**Choose the outcome before choosing the traits.**

::: notes
方針メモの「分布、成長、生存、共存、生態系機能」を、応答変数と検証方法に分けて示す。表は研究設計の例であり、万能な推奨形質リストではない。
問い：「干ばつに強い植物を探すとき、“強い”とは生存、成長維持、被度維持のどれ？」
分布の相関だけで耐性の機構や共存を示せるとは限らないことを短く予告する。
:::

---

## 02 | From a trait to a prediction

**Trait → process → performance in a specified environment**

- **Trait:** leaf mass per area, LMA
- **Process hypothesis:** investment in leaf construction and maintenance
- **Performance:** carbon gain, growth, or survival
- **Context:** light, water, nutrients, and neighbours

**What must be true for this trait to predict this outcome?**

::: notes
図案：4つの箱。Trait→Process→Performanceを横に置き、Environmentから各矢印へ線を引く。これは因果関係を確定した図でなく、検証したい仮説の図。
LMAは単位葉面積あたりの乾燥質量であり、LMAだけから建設コスト・維持呼吸・寿命が一意に決まるとは言わない。同じLMAの中身が異なる可能性を13へつなぐ。
:::

---

## 03 | Turn a trait association into a test

**Hypothesis:** leaf investment changes the balance between carbon gain and leaf persistence.

- Measure traits and performance on the same individuals.
- Compare responses across light or water conditions.
- Account for plant size and species identity.
- Test predictions on individuals or sites not used to fit the model.

**A correlation suggests a hypothesis; a design tests its predictions.**

::: notes
問い：「日向と日陰の葉を一緒にして相関を出すと、何を取り違える？」
実験操作、反復測定、観察データで可能な検証を区別する。予測精度が上がっても因果機構が確定するわけではない。未知の種・地点へ一般化したいなら、その単位でデータを分ける。
:::

---

<!-- Slide 04–06 | LES の後 -->
## 04 | Leaf economics is one part of plant strategy

- LES summarizes coordination among leaf traits.
- Whole-plant and organ size add another major dimension.
- A leaf strategy alone does not describe the whole plant.

**Similar leaf economics can occur in plants with different sizes and life histories.**

Source: [Díaz et al. 2016, Nature](https://doi.org/10.1038/nature16489)

::: notes
6形質の全球解析で、主要な変異がサイズと葉の経済性に関わる2軸に整理された事例。選んだ6形質から得た空間であり、植物の全戦略が完全に2次元だとはしない。
図案：サイズ×葉の経済性の概念図。4象限に樹木・草本の模式シルエットを置く場合も、実測点や論文のPCAスコアと誤認させない。「Conceptual illustration」と明記。
:::

---

## 05 | Roots add a collaboration dimension

- **Conservation:** contrasting investment in root tissue and metabolism
- **Collaboration:** direct resource acquisition versus greater reliance on mycorrhizal fungi
- These dimensions cannot be represented by one fast–slow axis.

**How resources are acquired matters as well as how rapidly they are used.**

Source: [Bergmann et al. 2020, Science Advances](https://doi.org/10.1126/sciadv.aba3756)

::: notes
1,810種の根形質解析。図案：横軸collaboration、縦軸conservation。細く長い根による直接獲得と菌根への依存を模式的に対比する。
葉のfast–slow軸と根のconservation軸の完全な一致は仮定しない。菌根タイプ・測る根の次数なども研究設計上重要。菌根への依存が大きければ常に成長が速い、という図にはしない。
問い：「同じ資源を、自分の根で探す植物と菌に投資する植物では、何を測れば違いが分かる？」
:::

---

## 06 | Match the organ to the ecological question

| Question | Traits to consider |
|---|---|
| Establishment after disturbance | Seed mass, germination, dispersal |
| Competition for light | Height, crown architecture, leaf deployment |
| Water limitation | Hydraulic vulnerability, stomatal regulation, rooting depth |
| Herbivore pressure | Chemical defences, toughness, tissue replacement |

**Trait choice should follow a process hypothesis.**

::: notes
前2枚の論文結果に含まれない水利用・防御も、研究設計の例として提示する。いずれも単独形質で結果が決まるとはしない。
ミニ課題：学生に1行選んでもらい、「環境をどう測るか」「どんな応答を追うか」を1つずつ答えてもらう。
:::

---

<!-- Slide 07–10 | Functional richness の前 -->
## 07 | Traits vary within species as well as among species

- A leaf measurement describes a particular leaf and individual.
- A species mean summarizes a sampled population of measurements.
- A community mean also depends on which species are abundant.

**A relationship at one level need not hold at another.**

::: notes
図案：葉・個体→種→群集の入れ子。種平均を「種に固有で不変な定数」として扱わない。
種平均のデータベースが不適切なのではなく、問いの階層と必要な変異の対応を考える。後半の既存Osnas et al.の図で、実際の階層間の違いを回収する。
:::

---

## 08 | Separate within- and among-species relationships

For individual \(i\) of species \(s\):

\[
t_{is}=\bar t_s+(t_{is}-\bar t_s)
\]

- **Among species:** how species means differ
- **Within species:** how individuals differ from their species mean
- These components can have different associations with performance.

::: notes
式は形質値の分解という恒等式で、因果モデルではない。図案：3種を色分けし、種内の回帰線と種平均同士の回帰線を別々に描く。描く値は仮想値と明記し、傾きの符号は実証結果として提示しない。
式の説明に時間をかけすぎず、同種内の光環境への応答と種間の違いを混ぜないことを伝える。
:::

---

## 09 | Community mean and trait variation answer different questions

\[
\mathrm{CWM}=\sum_s p_s t_s,\qquad \sum_s p_s=1
\]

Illustrative communities: three equally abundant species; trait values in arbitrary units.

| Community | Trait values | CWM | Weighted variance |
|---|---|---:|---:|
| A | 50, 100, 150 | 100 | 1,666.7 |
| B | 100, 150, 200 | 150 | 1,666.7 |
| C | 80, 100, 120 | 100 | 266.7 |

**A mean can shift without a change in variation, and variation can change without a shift in the mean.**

::: notes
授業用の仮想例。分散は \(\sum_s p_s(t_s-\mathrm{CWM})^2\) とし、不偏標本分散ではない。
図案：3本の横軸に種の点と平均の縦線を描く。A→Bは位置の移動、A→Cは幅の縮小。functional richnessとweighted varianceは同じ指標ではなく、ここでは「平均と広がりの問いの違い」を示す。
口頭で「どちらが多様か」ではなく「どの側面が変わったか」を尋ねる。
:::

---

## 10 | A CWM shift does not require trait change

Illustrative example: two species with fixed trait values.

| Species | Trait | Initial relative abundance | Later relative abundance |
|---|---:|---:|---:|
| A | 50 | 0.50 | 0.25 |
| B | 150 | 0.50 | 0.75 |

**CWM: 100 → 125, with no change in either species' trait value.**

- Species replacement or abundance shifts can change CWM.
- Within-species trait shifts can also change CWM when measured.

::: notes
この仮想例では、種数とtrait rangeは不変。一方、存在量で重み付けした分散は変わるので「多様性はすべて不変」とは言わない。
実データの重みが個体数・被度・バイオマスのどれかを確認する。後半の既存BCI事例で「誰の存在量が変わったか」と「なぜ変わったか」を分けて検討する。
:::

---

<!-- Slide 11 | Community assembly and trait distribution の後 -->
## 11 | Similar trait patterns can arise from different processes

- Environmental constraints can favour a narrow trait range.
- Competitive hierarchies can also favour a narrow trait range.
- Resource partitioning or enemy interactions can favour differences.

**A dispersion pattern is evidence to explain, not a unique diagnosis of a process.**

Source: [Levine et al. 2025, Trends in Ecology & Evolution](https://doi.org/10.1016/j.tree.2024.10.002); see also the existing competitive-hierarchy examples.

::: notes
これは後の既存スライド `How ecological processes might influence community assembly` と `Competitive hierarchy` を理解するための予告。ここで全メカニズムを教え直さない。
問い：「traitが似た種ばかり残った。環境が選んだ以外の説明は？」
帰無モデルの種プール・空間スケール・形質選択で判定が変わることも口頭で添える。既存の環境フィルタリング事例は「整合的な証拠」として扱う。
:::

---

<!-- Slide 12–14 | 既存の種内・種間の実証図の後 -->
## 12 | What does the same LMA value represent?

\[
\mathrm{LMA}=\frac{\text{leaf dry mass}}{\text{leaf area}}
\]

- LMA describes total mass investment per unit leaf area.
- This total includes tissues with different physiological roles.
- Equal LMA need not imply equal metabolic capacity.

**A useful summary can combine distinct biological components.**

Source: [Katabuchi et al. 2025, Oecologia](https://doi.org/10.1007/s00442-025-05714-3)

::: notes
既存の「種内と種間で関係が違う」図を指し、同じ変数名でも変動している成分が違うのではないか、と問う。種内では光環境に伴う代謝成分の変動、種間では構造的な違いも考える。
図案：同じ高さの2本の積み上げ棒を、異なる色配分で示す。実測値ではない概念図。組織を実際に2つに切り分けて秤量した結果とは説明しない。
:::

---

## 13 | Decompose LMA using a physiological model

\[
\mathrm{LMA}=\mathrm{LMA}_{m}+\mathrm{LMA}_{s}
\]

- **Metabolic component:** linked to photosynthetic capacity and respiration
- **Structural component:** linked to toughness and potential leaf lifespan
- Both components are inferred within a statistical modelling framework.

**Use processes to interpret the trait, rather than treating total mass as one investment.**

Source: [Katabuchi et al. 2025, Oecologia](https://doi.org/10.1007/s00442-025-05714-3)

::: notes
論文では潜在成分を統計モデルで推定している。「直接測定した形質が2つ増えた」とは言わない。予測値に対する評価では、応答変数が成分推定に使われていないか、学習・評価データの分け方も確認する。
ここでは推定法の詳細でなく、形質の意味を分ける発想を伝える。モデルの仮定と推定の不確実性は残る。
:::

---

## 14 | Improved physiological prediction has a defined scope

- LMA decomposition improved prediction of photosynthesis, respiration, and leaf lifespan in the study.
- This helps explain why within- and among-species patterns differ.
- Predicting coexistence requires further links to demography and competition.

**Better prediction of leaf physiology does not by itself demonstrate better prediction of coexistence.**

Source: [Katabuchi et al. 2025, Oecologia](https://doi.org/10.1007/s00442-025-05714-3)

::: notes
この直後に既存の `Using harder-to-measure physiological traits may not be enough` とLMA分解の結果図を置く案。前者は「さらに共存を問うなら何が足りないか」、後者は「葉の生理では何が改善したか」として読む。
既存 `images/gl_point.png` を結果図として活用可能。転載・新たな数値化は本下書きでは行っていない。予測改善率などの数字は論文の評価方法を対応付けるまで追加しない。
:::

---

<!-- Slide 15 | 既存のLMA分解の結果図の後 -->
## 15 | Coexistence requires a link to population dynamics

**Traits + environment + demographic processes → performance when rare**

- Competition depends on resource supply and resource use.
- Multiple traits and demographic rates can act together.
- Process-informed metrics connect these quantities through a model.

**Ask how traits affect the growth of a rare population among resident competitors.**

Source: [Levine et al. 2025, Trends in Ecology & Evolution](https://doi.org/10.1016/j.tree.2024.10.002)

::: notes
PIMを単なる「精密に測る形質」の別名にしない。共存の予測に必要な量を機構モデルから考える、という論文の主張として紹介する。
この講義でいうperformanceが葉の光合成、個体の成長、集団の侵入増殖率の間で変わっていることを明示する。侵入増殖率の解釈はモデルの仮定に依存するため、単一の指標だけであらゆる共存を判定できるとはしない。
LMA分解をLevineらの共存用PIMとして実証済み、と位置付けない。
:::

---

<!-- Slide 16 | 発展事例を使う場合はその後 -->
## 16 | Design a trait-based study

Choose one question: **distribution, drought response, coexistence, or ecosystem function**.

1. Define the response variable and its time scale.
2. Choose a trait and explain the process it represents.
3. Identify the sampling level: leaf, individual, species, or community.
4. State one alternative explanation and one test.

**“I will measure ___ to predict ___ because ___; I will test this by ___.”**

::: notes
2分でペア相談、1–2組に発表してもらう。「SLAを測って機能多様性を計算する」で止まる場合、何を説明・予測したいかに戻す。
短縮版では口頭の問いだけでもよい。前半の01に戻り、traitのリストや指標の公式でなく、研究の問いと検証方法が持ち帰りになるように締める。
:::

# 発展スライド：2026年の事例から必要なものを選ぶ

<!-- Slide 17 | drought response -->
## 17 | Trait–drought relationships depend on the plant group

- An extreme-drought experiment covered 63 sites and 421 species.
- The response was plant cover after one year of drought.
- Trait associations differed with growth form and lifespan.

**A prediction for one plant group need not transfer to another.**

Source: [Worthy et al. 2026, Nature Ecology & Evolution](https://doi.org/10.1038/s41559-026-02989-4)

::: notes
先に「資源保全的な形質をもつ植物ほど被度を維持する？」と予想させる。その後、生活形・寿命・形質の組合せで関係が異なることを紹介する。
草地・低木地の63地点、421種・661集団を扱う研究。樹木の長期死亡率、干ばつ後の回復、森林の耐乾性一般まで結論を広げない。各形質の効果の符号を見せるなら、該当群の結果図を選んでから注記する。
本文の数値・応答・条件依存性は論文要旨と著者側公開情報で確認済み。授業用の具体的なパネルは未選定。
:::

---

<!-- Slide 18 | CWM and prediction -->
## 18 | Global trait maps are predictions with a sampling history

- Combine trait records, vegetation surveys, citizen observations, and Earth observation.
- Predict global community-mean trait patterns for 31 traits.
- Evaluate geographic transferability using spatial validation.

**What does a map cell represent, and where is the prediction well supported?**

Source: [Lusk et al. 2026, Nature Communications](https://doi.org/10.1038/s41467-026-68996-y)

::: notes
方針メモの「31形質のCWM地図」を紹介しつつ、入力データを区別する。植生調査の存在量に基づくCWMと、市民科学記録から得るtrait meanは同じ観測量ではない。後者の記録頻度をそのまま真の存在量とはしない。
ここでの論点はCWMの地図＝個体形質の直接測定でも、多様性の地図でもないこと。空間的な外挿、欠測形質、サンプリングの偏りを問いにする。
図案：データ源→群集要約→予測地図の流れ。対象形質による精度の違いを消して「31形質が同精度」とは説明しない。
:::

---

<!-- Slide 19 | multiple biodiversity dimensions -->
## 19 | Biodiversity trends depend on the dimension and habitat

- Compare taxonomic, functional, and phylogenetic diversity over time.
- A European synthesis analysed 57,390 vegetation-plot time series.
- Interpret trends separately for different habitat types.

**What would species richness alone leave unresolved?**

Source: [Kambach et al. 2026, Nature Communications](https://doi.org/10.1038/s41467-026-72112-5)

::: notes
冒頭の「なぜ複数の多様性を測るか」を回収する。種数の増減だけでは、形質空間のどこが変わったか、どの系統が増減したかは分からない。
57,390は植生プロットの時系列数で、単発の全観測数ではない。結果を単純な「欧州の多様性は回復／減少」にまとめず、生息地ごとの差を読む。
図案：論文の生息地別比較から対象を絞る。すべての多様性次元で逆方向の変化が生じた、といった未確認の単純化を加えない。
:::

# 既存スライドに反映する際の検討事項（今回は変更しない）

1. **歴史の位置付け**：`Species + Site information + Species information (2000s ~)` はtrait研究の起源と読まれないよう、「群集生態学での統合・普及」を指す注記を検討する。
2. **LESの射程**：現在の「Global leaf function constrained to a single axis」「Multidimensional ... mapped into a one-dimensional index」は、特定データの形質共変動の要約であると補う。04・05に接続すれば、葉や植物全体の機能が1軸に還元できるという誤解を防げる。
3. **パターンと過程**：クラスタリング＝環境フィルタリング、過分散＝limiting similarityを一対一の判定規則として読ませない。11を予告にし、後のcompetitive hierarchyで具体化する。
4. **CWMの重複**：09・10は概念、既存BCIスライドは実例と役割を分ける。既存の病原体の説明は仮説・証拠の強さに合わせて述べる。
5. **LMA分解の重複**：12・13で問いとモデルを説明し、既存の結果図で14を具体化する。統合時には14と既存結果スライドを1枚にまとめる選択肢があるが、本稿では結果図を変更しない。
6. **PIMの射程**：既存 `PIMs (LMAm/LMAs) outperform bulk LMA for predicting physiology` は、共存用PIMの実証と混同されやすい。`LMA decomposition improves physiological prediction` と述べる案を検討する。スラッシュが比率を意味するようにも見えるため、2成分を意味する場合は `LMA_m and LMA_s` と書く。
7. **Levine論文の年**：既存では2024と記載。オンライン公開は2024年、巻号は2025年（40巻2号147–158頁）。本稿は巻号に合わせ2025で統一した。
8. **発展事例の時点**：既存資料の開催日表記は2025年。17–19は2026年以降の授業への追加として扱う。日付の更新は本稿では行わない。

# 参照文献と確認範囲

以下は本文・要旨・著者公開版等で主張を確認した一次資料。図の転載、効果量の再計算、結果パネルの最終選定は行っていない。リンクは各スライドにも付した。

- Díaz, S. et al. (2016). *The global spectrum of plant form and function*. Nature 529, 167–171. https://doi.org/10.1038/nature16489
- Bergmann, J. et al. (2020). *The fungal collaboration gradient dominates the root economics space in plants*. Science Advances 6, eaba3756. https://doi.org/10.1126/sciadv.aba3756 （[本文公開版](https://pmc.ncbi.nlm.nih.gov/articles/PMC7458448/)）
- Katabuchi, M. et al. (2025). *Decomposing leaf mass into metabolic and structural components explains divergent patterns of trait variation within and among plant species*. Oecologia 207, 71. https://doi.org/10.1007/s00442-025-05714-3 （[著者公開版](https://people.clas.ufl.edu/jlichstein/files/Katabuchi_etal_2025_Oecologia.pdf)）
- Levine, J. I. et al. (2025; online 2024). *Why ecologists struggle to predict coexistence from functional traits*. Trends in Ecology & Evolution 40, 147–158. https://doi.org/10.1016/j.tree.2024.10.002
- Worthy, S. J. et al. (2026). *Growth form and lifespan of herbaceous species mediate the role of traits in short-term drought response*. Nature Ecology & Evolution 10, 512–522. https://doi.org/10.1038/s41559-026-02989-4 （[著者公開版](https://justinluong.com/assets/pdf/Worthy%20et%20al%20Nature%20EE%202026.pdf)）
- Lusk, D. et al. (2026). *Crowdsourced biodiversity monitoring fills gaps in global plant trait mapping*. Nature Communications 17, 1203. https://doi.org/10.1038/s41467-026-68996-y
- Kambach, S. et al. (2026). *Habitat-specific trends in taxonomic, functional, and phylogenetic diversity in European plant communities over a century*. Nature Communications 17, 4208. https://doi.org/10.1038/s41467-026-72112-5
