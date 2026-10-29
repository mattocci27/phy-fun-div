# Simpsonの計算過程・Anole模式図・英語ノート

日付：2026-10-29  
プロジェクト：phy-fun-div

## 目的

数学が苦手な学生も計算を追えるS8と、機能的類似性と系統的類似性の不一致を読み取れるAnoleの図に整える。最後に全speaker notesを英語に統一する。

## 現在の状態

- `main.qmd` を修正し、Quartoのrevealjs出力を再生成済み。全67枚。
- S8とAnole統合版は、通常のChromeで実際のスライド画面を開いて見た目を確認済み。
- ノート英訳後もレンダリング成功。`main.html` と `main-speaker.html` の全40ノート欄に日本語が残らないことを検証済み。
- コミット・pushはしていない。既存の未コミット変更は保持。

## 決定と理由（やり直さないこと）

### S8：数値代入を必ず残す

- 以前のログにある「途中計算は出さない」は、今回のユーザー指示で上書き。
- 4種の個体数4、300、56、23、合計383を使い、次の2段階を表示する。
  - `Σp_i² = (4/383)² + (300/383)² + (56/383)² + (23/383)² ≈ 0.639`
  - `1/Σp_i² = 1/0.639 ≈ 1.57`
- 二乗和は2項ずつ2行。スラッシュ表記、aligned環境、フォント0.75emで50%幅の右カラムに収めた。左の表・グラフは変更していない。
- 丸め前の値は二乗和0.638636844、逆数1.565835121。

### スライド整理

- 旧S20「Phylodiversity」（Faith 1992の歴史的説明）を削除。
- 元のAnole 2枚はそのまま残し、その直後に統合版を追加。削除1枚・追加1枚なので総数67枚。
- 統合版は現在S26、ID `anole-combined`。
- タイトルはユーザー指定の **Do phylogenetically related species have similar ecological niches?**。
- ほかに提案したS19、S4、S16–18、S42などの整理は採用していない。勝手に変更しない。

### Anole模式図の最終仕様

- 統合版の左側のトカゲ写真は維持。右側の図をRチャンク `anole-schematic` で生成。
- 途中で6種版を作ったが、最終指示により **12種（3 ecomorphs × 4島）** に戻した。6種・9種へ減らさない。
- 島は架空のIsland A–D。先端はA–D、色と文字の組み合わせで同じ種を左右で識別する。
- Crown-giant `#0072B2`、Trunk-ground `#D55E00`、Twig `#882255`。混合する内部枝は `#333333`。
- 左はecomorphごとの4種がまとまり、右は島ごとに異なるecomorphが近縁になる説明用の構成。
- 枝の縦コネクタが子の色を継承するggtreeの挙動を補正し、混合ノードの縦枝をグレーで重ね描き。
- 左右は同じ描画範囲・高さ。凡例は2樹の下に1つ。大きな先端ラベルを使用。
- 生物学的結論はLosos et al. (1998)に基づくが、樹形・枝長・島間関係・移住経路の再現ではない。スライドとノートの両方に明記。

### Speaker notes

- 全40ノート欄を点検し、日本語部分を英訳。数式・数値・帰無モデルや解釈上の注意点を保持。
- タイトルスライドの無意味なプレースホルダー `hoge` を除去し、ノート欄自体は保持。
- ノート以外の本文が変化していないことを、ノート欄を除外したソース比較で検証。
- 既存の英語ノートは基本的に保持。本文・ノートともに新規の科学文献調査は行っていない。

## ファイル

- 編集：`main.qmd`
- 生成・更新：`main.html`、`main-speaker.html`、`figure/anole-schematic-1.png`、レンダリングに伴う一部生成画像。
- 新規：本ログ。既存のレビュー文書・過去ログ・作業開始前の変更はそのまま。
- `main.knit.md` はQuartoの中間生成物で、レンダリング中に生成・削除されることがある。ログ作成時点のgit statusでは変更扱い。手動で復旧・削除していない。

## レンダリングと確認方法

- 通常のコマンド：`RENV_CONFIG_AUTOLOADER_ENABLED=FALSE R_LIBS=renv/library/macos/R-4.6/aarch64-apple-darwin23 quarto render main.qmd --to revealjs`
- このセッションではmacOSのQuarto Sassキャッシュが書き込み制限で `unable to open database file` となった。`XDG_CACHE_HOME` はmacOS側のキャッシュパスには効かなかった。
- 一時コピー `/private/tmp/s8-inverse-simpson/quarto.js` の `darwinUserCacheDir()` だけを一時領域へ向け、付属Denoで実行してレンダリング成功。インストール済みQuarto本体やシステム環境変数HOMEは変更していない。
- 実行時には `QUARTO_BIN_PATH=/Applications/quarto/bin`、`QUARTO_SHARE_PATH=/Applications/quarto/share`、`DENO_DOM_PLUGIN=/Applications/quarto/bin/tools/aarch64/deno_dom/libplugin.dylib`、`DENO_TLS_CA_STORE=system,mozilla` と上記R環境を指定。Denoは `/Applications/quarto/bin/tools/aarch64/deno run --v8-flags=--enable-experimental-regexp-engine --unstable-ffi --unstable-kv --no-config --no-lock --allow-all`。
- 一時ファイルの存続は保証しない。通常環境では通常のQuartoコマンドを先に試す。
- ヘッドレスChrome/Firefoxはこの環境で終了コード134、ブラウザー接続ホストも使用不可。`cua.getApp("com.google.Chrome")` のネイティブ操作は利用できた。
- 表示URL：`file:///Users/mattocci/Workspace/1-Projects/phy-fun-div/main.html?fragments=false#/anole-combined`。S8のIDは `a-first-order-properties-abundance`。

## 未解決事項・次の作業

- 今回依頼された編集は完了。次は必要に応じてユーザーが通常の発表・speaker viewで確認する。
- 以前からのEndara図の縦軸の符号確認、LES図や補足スライドのレイアウト課題は未対応。今回の範囲では変更していない。
- 最終のノート英訳ではソース・生成HTMLを検証したが、speaker viewの40ノートを画面で1つずつ読んだわけではない。
- ユーザーから指示があるまでコミット・pushしない。
