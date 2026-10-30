3本を読んで比較すると、どれもTrait-based Ecologyの授業で使う価値があります。ただし、学生に理解させたい概念がかなり違います。

私なら、Worthy et al. (2026) を最優先にします。Traitが植物のperformanceを予測できるのかという、trait-based ecologyの中心的な問いを直接検証しているからです。

一方、LuskはCWMの空間予測、Kambachはfunctional diversityと生物多様性の時間変化に焦点を当てています。

## まず3本の比較

| 論文                                       | 中心的な問い                             | 授業での評価    |
| ---------------------------------------- | ---------------------------------- | --------- |
| Worthy et al. Nature Ecology & Evolution | Traitから干ばつ抵抗性を予測できるか？              | 最優先       |
| Lusk et al. Nature Communications        | 種の分布記録から全球のCWMを予測できるか？             | CWMの応用に最適 |
| Kambach et al. Nature Communications     | 種数が増えるとfunctional diversityも増えるのか？ | 討論に最適     |

3本を通じて、次のような流れを作れます。

Worthy：Trait → Performance

形質は植物の環境応答を説明できるか

Lusk：Trait → Community composition

群集の平均形質は全球でどう分布するか

Kambach：Trait diversity → Biodiversity change

機能的多様性は時間とともにどう変化するか

以下、研究結果だけでなく、論文の弱点と授業での使い方まで掘り下げます。

## 1. Worthy et al. (2026)

Growth form and lifespan of herbaceous species mediate the role of traits in short-term drought response — Nature Ecology & Evolution

一番面白いのは、「保守的な形質を持つ植物ほど干ばつに強い」という単純な予測が支持されなかったことです。

### 研究の目的と方法

世界63地点の草原・低木群落で、約1年間の極端な干ばつ実験を実施。421種、661個体群（種×地点）のデータを使って、9つのfunctional traitsが干ばつ応答を説明するか検証しています。

干ばつ抵抗性は、植物の生存率や水ポテンシャルではなく、対照区に対する被度の変化で評価しています。

\\[ \Delta C=(D\_{\mathrm{after}}-D\_{\mathrm{before}}) -(C\_{\mathrm{after}}-C\_{\mathrm{before}}) \\]

つまりBACIデザインです。正の値ほど干ばつ区の相対的な被度変化が大きいことを示します。

形質はleaf N、SLA、plant height、root tissue density (RTD)、specific root length (SRL)、root mass fraction (RMF)、rooting depthなど。解析には地点と種のrandom effectsを含むBayesian linear mixed model（`brms`）を使っています。

Worthy_et_al_2026(1).pdf



### 主な結果

[Trait-mediated demographic response to drought in the Colorado shortgrass steppe | Alice Stears](https://images.openai.com/static-rsc-4/dG4u91TbnpuSud1Tao9WjX7b2fSXqZPYPOva1uG2UR-vgjmlSA6-BOlvac9pelu4zbijtkKkuYDzH8GFgud0DtRwvDtV5bnTtIiIe_6A_s9uZd9xJX_TnkEg2EG1oIxGLF4d7z4H1xaKbitFMN67lue5CgeyWx9XTZDsWKNGx6M?purpose=inline)

Fig. 2：単独の形質の効果

全種をまとめると、leaf Nが高いほど干ばつ抵抗性が高い。Forbs（広葉草本）では、さらに草丈とRTDが高い種ほど抵抗性が高い。一方、graminoids（イネ科型草本）では有意な形質が見つかりませんでした。

[树种地上和地下性状研究进展----中国科学院西双版纳热带植物园](https://images.openai.com/static-rsc-4/N-1v7NV008HeWdGCABmLP1vnBcfrcZCin2Xv_Oi6JILCpY-kZmTwzBBZ7G4H-cYfobVsCBDdTVraeRmchDgef_CFoXvyH_1PuctiMLFGU3rND8shCPFhyHVR0J5JLE2HVzYHUwIZyBHVR-lSvYgDaFvSkDdNVqNY_-558bl4BbI?purpose=inline)

Fig. 3：形質の組み合わせ

高いleaf Nと高い草丈、または高いleaf Nと大きなRMFの組み合わせが有利。Forbsでは、高RTD・低SRLと低RTD・高SRLの両方が高い抵抗性と関連し、複数の戦略が同様のperformanceにつながる可能性が示されました。

[Neighbourhood diversity increases tree growth in experimental forests more in wetter climates but not in wetter years | Nature Ecology & Evolution](https://images.openai.com/static-rsc-4/8T9hizKAZFTaP5QvsTJZkDrXDLGteLQMzlCpc_sHcDUW8EVZ6H0LtwpnRM2Q6oRWDZ2PWSdogxAd7nAK0B0RLeLXiM9c1-cq6BAkOFw-aCMqJ9IjPc0tNJ2PuDqvxFi7rPVyfmsinzkIIMRdIZyzS_bNpS2xNHVPdRU-wJix5lY?purpose=inline)

Fig. 4：環境による効果の変化

Leaf Nが高いことの有利さは、干ばつが比較的弱い条件で現れる。年間降水量の多い地点では、背の高い一年草ほど抵抗性が高い傾向も示されています。

参照すべき原著図：Worthy et al., Fig. 2（PDF p.3）、Fig. 3（p.4）、Fig. 4（p.5）。上の画像は図を探すための参考画像です。

ここが授業向きです。Fast–slow spectrumを教えた学生なら、最初は低SLA、低leaf N、高RTDの植物が干ばつに強いと予想するかもしれません。しかし、結果はもっと複雑です。

著者らは、短期的な干ばつでは素早い成長や繁殖による drought escape が有利になり得る一方、保守的な根への投資も役立つと解釈しています。

Worthy_et_al_2026(1).pdf



### 論文の弱点と注意点

私が特に気になるのは説明率の低さです。

Fig. 2の全種モデルは \\(R^2=0.06\\)、forbsでも約0.12。Fig. 3の交互作用モデルも多くが0.05〜0.13です。統計的に有意な効果はありますが、traitから干ばつ応答を十分に予測できる段階ではありません。

さらに、観測されたtraitは種平均値で、すべての実験地点で測定されたものではありません。約48%のtraitデータは補完されており、50回のimputationの平均値が解析に使用されています。したがって、種内変異やimputationの不確実性が十分に反映されていない問題があります。

Worthy_et_al_2026(1).pdf

Worthy_et_al_2026(1).pdf



また、被度変化には生存、成長、フェノロジー、競争相手の減少などが混ざります。「高leaf Nが干ばつ耐性を高める」という生理学的な因果関係が証明されたわけではありません。

### 授業での使い方

最初にfast–slow spectrumから予測を立てさせ、Fig. 2を見せる。その後、Fig. 3でtrait interactionを紹介するのが良さそうです。

最後に、\*\*「では、なぜ全球421種のデータを使っても説明率が6%しかないのか？」\*\*と問いかける。

これだけでtraitの選択、環境依存性、種内変異、観測していない生理特性まで議論できます。

&#x20;授業採用：強くおすすめ。30〜40分程度のケーススタディに向いています。

## 2. Lusk et al. (2026)

Crowdsourced biodiversity monitoring fills gaps in global plant trait mapping — Nature Communications

この論文の本質は、測定していない場所の群集平均形質を、種の出現記録と環境情報から予測できるということです。

### 研究の目的と方法

データソースは主に3つです。

- TRY： 種ごとの形質値
- sPlot： 群集内の種組成と相対被度
- GBIF： 市民科学などから収集された種の出現記録

これらにMODIS、WorldClim、SoilGrids、樹冠高などの環境情報を組み合わせ、LightGBMで31種類のtraitの全球分布を予測します。最も細かい解像度は約1 kmです。

重要なのは、sPlotとGBIFでは計算される平均が異なることです。

sPlotでは通常のCWM：

\\[ \mathrm{CWM}\_{j}=\sum_i p\_{ij}t_i \\]

ここで \\(p\_{ij}\\) は種 \\(i\\) の相対被度です。

一方、GBIFでは：

\\[ \bar t_j^{\mathrm{GBIF}}= \frac{\sum_i n\_{ij}t_i}{\sum_i n\_{ij}} \\]

\\(n\_{ij}\\) は種 \\(i\\) の観測記録数であり、植物の実際のabundanceではありません。

それでも大量の出現記録が、群集の形質構成を推定するproxyとして機能するか検証しているわけです。

Lusk_et_al_2026(1).pdf



### 主な結果

[Crowdsourced biodiversity monitoring fills gaps in global plant trait mapping | Nature Communications](https://images.openai.com/static-rsc-4/0C55nbrxKkYaSJkbYUC688VcPQWOD9ef5gl4KZW8RBY6wa14CZLxt0QLwpmH3fTPCCkKp73xF0QR6d0nVeMUNDH9seaLpN91_dyvjTz0IPLfP82QNGPFyFFKZigZkXVrIBeRuiCixHiKkCqTRPlZz3P9LVIbp9zWy51yDodgpEU?purpose=inline)

Fig. 2：研究の全体像

種の出現記録とtraitデータから形質の空間的平均を作り、環境データを説明変数として全球に外挿する仕組み。授業で最もわかりやすい図です。

[Crowdsourced biodiversity monitoring fills gaps in global plant trait mapping | Nature Communications](https://images.openai.com/static-rsc-4/3d60D8jrNcyhNrU4tXhGqY-_cIGA_4B9HosH4EtEFaVFgcsoC670CNKhRz48KeGfr39_HV-fNBDqTLitepnVJzLsesqqkZ8c_7wnu-_rWiCUB6dlODFL64VYMrPUacIBmZRuO0fPZuqA6iR-7kxDjKOmpbxsPR8zge4uNkN2WMI?purpose=inline)

Fig. 4：市民科学データを加える価値

GBIFを追加すると、予測の適用可能領域（AOA）が平均2.43パーセントポイント増加し、cross-validation間の予測変動も小さくなりました。

原著のFig. 2（PDF p.3）とFig. 4（p.6）が教材候補。詳細な精度比較はFig. 5（p.7）。

ここで面白い結果があります。

1 km解像度で予測精度が \\(r\geq0.5\\) となったtraitは、sPlotだけ（SCI）では31形質中16形質、統合データ（COMB）では15形質。つまり、GBIFを追加したからといって、独立検証データに対する平均的な予測精度が高くなるわけではありません。

それでもGBIFを追加する意味はあります。sPlotが不足している地域で、予測できる環境条件の範囲が広がるためです。

Lusk_et_al_2026(1).pdf



### 論文の弱点と注意点

特に授業で指摘したいのは次の3点です。

① GBIFの頻度はabundanceではない。

写真を撮られやすい植物、道路沿いの植物、同定しやすい植物が過大評価されます。観測頻度で重み付けした平均を、そのまま真のCWMと同一視することはできません。

② 種内変異を扱っていない。

同じ種には世界中どこでも同じtrait平均値を割り当てています。群集構成の空間変化は表現できますが、個体・集団が局所環境に応じて形質を変化させる過程は反映されません。

③ 予測の適用可能性と精度は別物。

AOAは、新しい場所の環境条件が学習データにどれほど似ているかを評価するものです。また、ここでのCOVはcross-validationのモデル間変動であり、真のtraitの予測誤差をすべて表したものではありません。

著者も、これらのサンプリングバイアスや種内変異の問題を認めています。

Lusk_et_al_2026(1).pdf



### 授業での使い方

CWMを教えた直後に、「もし群集のabundanceがなく、species occurrenceしかなかったら？」と問いかけるとよいと思います。

その後、Fig. 2を使って研究の構造を説明し、Fig. 4・5で予測精度と外挿可能性の違いを議論する。

ただ、これはtrait–performance関係を検証した研究ではありません。主題はtrait mappingとデータ統合なので、授業の中心に据えるとremote sensingやmachine learningの解説が大きくなりそうです。

&#x20;授業採用：CWMを教えた後の15〜20分の応用例としておすすめ。

## 3. Kambach et al. (2026)

Habitat-specific trends in taxonomic, functional, and phylogenetic diversity in European plant communities over a century — Nature Communications

この論文の面白さは、「種数が増え、functional diversityも増えているのに、必ずしも生態系の状態が改善しているとは言えない」という点です。

### 研究の目的と方法

ヨーロッパ全域の植生調査から、57,390の時系列、199,282回の植生調査記録を統合しています。

種数（taxonomic diversity）に加えて、functional diversity、phylogenetic diversity、絶滅危惧種、外来種、habitat specialists/generalistsの変化を調べています。

Functional diversityには14のtraitを使用。TRYのgap-filledデータから選択して、functional richness、functional evenness、functional divergenceを計算しています。

時系列ごとに多様性指数の対数と年の回帰から変化率を求め、それらを統合して全体傾向を推定しています。

Kambach_et_al_2026(1).pdf

Kambach_et_al_2026(1).pdf



### 主な結果

ヨーロッパの植生群集における平均年間変化率

0%/年0.2%/年0.4%/年0.6%/年0.8%/年種数Functional richnessFunctional divergence系統距離 MPD系統距離 MNTD

Kambach et al. (2026), Fig. 1。各指標のベースラインに対する平均年間変化率。

原著Fig. 1の数値をもとに作成。Functional evennessには有意な増減が認められていません。指標ごとに尺度や解釈が異なるため、棒の高さを直接比較して生態学的重要性を判断するものではありません。

予測とは逆に、local species richnessだけでなくfunctional richnessやphylogenetic diversityも平均的には増えていました。

しかし、湿地での多様性増加には注意が必要です。

湿地が乾燥化すると、本来生育していなかった樹木や一般的な草本が侵入できるようになります。その結果、局所的な種数やfunctional richnessが増えても、湿地特有の植物群集は失われているかもしれません。

著者らも、湿地での多様性増加は環境の悪化を反映している可能性を指摘しています。

Kambach_et_al_2026(1).pdf



もう一つの重要な結果は、地域全体のgamma diversityには一貫した増加がなかったことです。安定した草地や遷移中の疎植生地では増加が見られましたが、全体としては明確な傾向がありませんでした。

これは、局所的な種数の増加と、広域的な生物多様性の増加が同じ意味ではないことを示しています。ただし、beta diversityの低下を直接検証した研究ではありません。

### 論文の弱点と注意点

この論文は、研究者の視点で読むとむしろ批判的検討に向いています。

① 「100年間の変化」の解釈。

最大103年の観測記録を含みますが、時系列の55%は観測が2回だけです。最初と最後の観測間隔も5〜10年が最も多く、実際に100年間継続観測した群集が多数あるわけではありません。

② 調査区の選択バイアス。

過去に存在した湿地や草地が完全に破壊されてしまった場合、再調査対象から外れやすい。これにより、多様性の増加傾向が過大評価される可能性があります。

さらに、半永久調査区では同一地点を厳密に再調査していない場合があり、species turnoverと位置の違いによる変化を完全には区別できません。

③ Habitat changeの分類は種組成にも依存する。

EUNISによるhabitat分類に種組成を利用しています。その分類から推定したhabitat transitionで、再び種組成に由来するdiversityの変化を説明しています。

そのため、habitat transitionとdiversity changeの関係を独立した環境要因の因果効果として解釈するのは難しいでしょう。

④ Functional richnessの増加をどう評価するか。

Functional richnessは種数に敏感です。新たな種が加入すればtrait spaceが拡大することもありますが、それだけで群集の機能的な健全性が改善したとは言えません。

また、論文ではrelative percentage changeと元の尺度でのannual changeで、Red List speciesなど一部指標の傾向の符号が異なっています。これは統計指標の選択自体が結論に影響する、良い教材になります。

Kambach_et_al_2026(1).pdf



### 授業での使い方

Functional diversityを教えた後に、以下の問いを学生に投げると面白いと思います。

> 湿地が乾燥化し、湿地特有の5種が減少して、一般的な草本と低木が10種増えた。Functional richnessが増加した場合、それは望ましい変化と言えるだろうか？

ここからspecies richness、FRic、functional composition、habitat specializationの違いを考えさせられます。

ただし、この論文そのものはtraitが環境応答を決める仕組みの検証よりも、多様性の記述と変化の統合が中心です。

&#x20;授業採用：Functional diversityを扱う回の20〜30分の討論教材としておすすめ。

## 最終的なおすすめ

授業のメイン教材にするか、紹介だけにするかで分けるなら、私はこうします。

|              | Worthy | Lusk  | Kambach |
| ------------ | ------ | ----- | ------- |
| Traitの生態学的意味 | 非常に強い  | 中程度   | 強い      |
| 仮説検証の面白さ     | 非常に強い  | 中程度   | 強い      |
| CWMとの関連      | 弱い     | 非常に強い | 中程度     |
| 学生へのわかりやすさ   | 比較的高い  | 中程度   | 中程度     |
| 論文を通読させる価値   | 高い     | やや専門的 | 高い      |

1本だけ必読にするならWorthy。 IntroからResultsまで読み、特にFig. 2〜4で予測がなぜ外れたのか考えさせたいです。

Luskはスライドで紹介するだけでも十分かもしれません。Fig. 2の研究フローを見せれば、CWMがどう全球のtrait mapにつながるか理解できます。必要なら [論文のインタラクティブな全球trait map](https://global-traits.projects.earthengine.app/view/global-traits?utm_source=chatgpt.com) を学生に見せるのもよいでしょう。

Kambachは学生の理解度が上がってから。 Traitの平均と分散、多様性指標の意味を理解した後でないと、単なる「ヨーロッパで多様性が増えた論文」として読まれてしまいそうです。

なお、この3本には共通する重要な限界があります。いずれも大規模なデータ統合において、種平均traitや補完traitに大きく依存しています。

授業全体を通したメッセージとしては、

「Traitは植物の生態を一般化するための強力な道具だが、traitの選択、種内変異、環境依存性、集約の方法によって、得られる生態学的結論が変わる」

というところに着地させると良いと思います。

私が特に学生と議論したいのは、Worthyの421種を使っても \\(R^2=0.06\\) という結果です。Trait-based ecologyが何を説明できて、何をまだ説明できていないのか。その議論こそ授業の核心にできそうです。
