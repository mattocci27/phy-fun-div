# Kambach・Worthyの配置とPIMへの流れ

日付：2026-10-30  
プロジェクト：phy-fun-div

## 目的

新規追加したKambach et al. 2026（ヨーロッパ植物群集の多様性変化）とWorthy et al. 2026（形質による干ばつ応答予測）のスライドについて、説明のタイミングと内容が学生の理解を深めるか確認し、改善する。あわせて、講義終盤（形質→生理→共存）の論文の順序を決める。

## 現在の状態

- `main.qmd` を修正し、`quarto render main.qmd` で `main.html` を再生成済み（今回は通常コマンドで成功。1回目は一時的にエラー、2回目で成功）。全66枚。
- Kambach・Worthyのスライドは、ヘッドレスChromeで全fragment表示の状態を目視確認済み。
- Levineスライドに追加したfragment bulletは、HTMLへの出力を確認済み。ただしスクリーンショットでは非表示のままで、画面上の収まりは未確認（右カラム下部に余白は十分ある）。前回ログの `?fragments=false` を使えば確認できるはず。
- `main-speaker.html` は今回再生成していない。
- コミット・pushはしていない。

## 講義終盤の最終スライド順

40 BCI CWM（Katabuchi 2017） → 41 Kambach 2026 → 42 Worthy 2026 → 43 Osnas 2018 → 44 Katabuchi 2025 → 45 Levine 2024 → Summary

## 決定と理由（やり直さないこと）

### Kambach（旧S33 → 現S41、ID `kambach-2026`）

- convex hull直後の位置から、BCIのCWMスライドの直後へ移動。
  - 旧位置では、Cornwell 2006 → Cornwell & Ackerly 2009 → Kraft 2008の「パターンから過程を推論する」流れが途切れていた。
  - 図に未習の指標（FDiv、CWM niche widthなど）が含まれていた。CWM niche widthは、CWMの説明より前に出ていた。
  - BCIの例と並べると、「集約した指標は、どの種が増減しているかを隠す」という同じメッセージを2回示せる。
- 3つ目のbulletを、図から直接読める事実に変更：generalists +0.41、non-native +1.23、specialistsは有意な変化なし。
- ノートに追加した内容：
  - 図を見せる前に予測させる問い
  - BCIとの対比
  - FRicの種数依存の復習。本文Methodsでは、14形質を単位分散に標準化して計算しており、種数を揃えたnull modelの記述はない
  - Red List種のcoverも+0.39増えているため、一様な劣化として提示しないという注意

### Worthy（現S42、ID `worthy-2026`）

- 「LES expectation（保守的な葉→干ばつに強い？）」→ Result「逆：高leaf Nほど抵抗性が高い」→「R² = 6%」→ take-home「Traits covary strongly with each other, yet predict performance weakly.」の順にfragmentで提示する。
- 作業中にユーザーが自分で編集した内容（footerの簡略化、「cf. LES 75%」の削除）は維持。元に戻さない。

### 終盤の順序（ユーザー選択：案3）

- 「Worthy → Osnas → Katabuchi 2025 → Levine」とし、「問題 → 原因 → 解決例 → 一般化」の流れにした。
- 不採用の案：
  - Levine → Katabuchi 2025の順：LMAm/LMAsを見せるときにスケールが共存から生理へ下がり、そこで終わってしまう。
  - 元の順序。
- **PIMの位置づけ（重要）**：Levineの図（`images/pim.png`）では、PIMはvital ratesとniche/fitness differenceの間にある。LMAm/LMAsは「論理はprocess-informedだが、まだ形質であり、軸の左端（Functional traits）」と説明する。「LMAm/LMAsはPIMの例」とは言わない。
- Katabuchi 2025のノートでは、予測対象は生理であり、Worthyの6%を解決するものではないと明記した。
- Levineスライドに追加したfragment：「**LMAₘ / LMAₛ:** process-informed in logic, but still a trait → left end of this axis.」
- ノートのつなぎを新しい順に合わせて書き換えた：
  - ロードマップ（S38）
  - Kambach → Worthy：「generalistが勝った。勝者を形質で予測できるか？」
  - Worthy → Osnas：「なぜ予測力が弱いか：種平均・バルク形質」
  - Levine：例を図の軸上に位置づけさせ、Worthyの94%に戻る

## ファイル

- 編集：`main.qmd`
- 再生成：`main.html`
- 参照（未追跡のまま）：`Kambach_et_al_2026.pdf`、`Worthy_et_al_2026.pdf`、`docs/additional_papers.md`、`images/kambach2026-diversity-trends.png`、`images/worthy2026-leaf-n.png`
- 新規：本ログ
- 一時スクリーンショットはセッションのscratchpadに保存（永続的な成果物ではない）。

## 未解決事項・次の作業

1. **最優先**：S45（Levine）のfragment bulletの表示と、S42（Worthy）のfragment箇所のインデントと行間を、実際の画面で確認する。fragment部分のbulletは別リストのため、わずかにインデントと行間が異なる。気になる場合は修正する。
2. Levine et al. 2024のPIMの定義を原著で確認する。説明はPIMが「生理レベルの指標を含まない」前提で書いている。
3. Kambachで、FRicを種数に対して標準化しているかをSupplementaryで確認する。
4. 必要なら `main-speaker.html` を再生成する。
5. Lusk et al. 2026（`docs/additional_papers.md` で検討）は未採用。追加する場合は、CWMの後の応用例として検討する。
