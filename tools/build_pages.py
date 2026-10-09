"""Generate JVM service and industry pages from PAGES below.

Run from the repo root: python3 tools/build_pages.py
Writes <slug>/index.html for each page and refreshes sitemap.xml.
"""
import html
import json
import os

BASE = "https://justvibingmedia.com/"
WA = "https://wa.me/85259932444?text=%E4%BD%A0%E5%A5%BD%EF%BC%8C%E6%88%91%E6%83%B3%E4%BA%86%E8%A7%A3%20JVM%20%E6%9C%8D%E5%8B%99"
EMAIL = "justvibingmedia8@gmail.com"

NAV = [
    ("ip/", "個人 IP"),
    ("social-media/", "IG・FB・Threads"),
    ("video/", "拍片・AI 內容"),
    ("google-maps/", "Google 地圖"),
    ("ai-seo/", "AI SEO"),
    ("meta-ads/", "Meta 廣告"),
]
INDUSTRIES = [
    ("industries/physio/", "痛症治療店"),
    ("industries/cafe/", "咖啡小食店"),
    ("industries/salon/", "髮型屋"),
]

PAGES = [
    {
        "slug": "ip/",
        "title": "打造個人IP｜香港小店老闆個人品牌｜Just Vibing Media",
        "desc": "JVM 幫香港小店老闆打造個人 IP：人設、口號、內容支柱、腳本，真人團隊上門拍片，IG、Facebook、Threads 發佈。老闆唔識拍片都做到個人品牌。",
        "eyebrow": "個人 IP 打造",
        "h1": "幫香港小店老闆打造個人 IP",
        "lede": "個人 IP 即係老闆自己嘅個人品牌：一個有性格、有觀點、客人認得出嘅人。貨品同價錢可以俾人抄，你呢個人冇人抄得到。JVM 由 IP 定位到每月拍片發佈，一條龍幫你做。",
        "blocks": [
            ("點解小店老闆要做個人品牌", [
                ("信任快啲建立", "客人喺 IG、Threads 睇過你講嘢，未入舖已經信你。"),
                ("唔使淨係鬥平", "客人係衝住你而嚟，唔會為平十蚊走去隔籬。"),
                ("內容唔會斷", "有固定人設同內容支柱，每月都知拍乜講乜。"),
            ]),
            ("你嘅 IP 方案包括", [
                ("人設同口號", "IP 名、一句口號、你同隔籬舖唔同嘅地方。"),
                ("定位同目標客", "講俾邊個聽、佢哋最痛嘅問題係乜。"),
                ("內容支柱", "3 至 4 類固定內容，例如專業知識、幕後、客人故事。"),
                ("腳本同分鏡", "我哋編劇寫好，老闆出鏡照住講就得。"),
                ("引流留客路徑", "由睇片、留言、WhatsApp 到上門，一步步帶客。"),
                ("排程同 KPI", "第一個月出乜、幾時出，用咩數字睇成效。"),
            ]),
        ],
        "faq": [
            ("咩係個人 IP？", "個人 IP 就係老闆自己嘅品牌：一個有性格、有觀點、客人認得出嘅人。JVM 幫你定人設、口號同內容方向，再每月拍片發佈，令客人因為你呢個人而揀你間舖。"),
            ("老闆唔識拍片、唔慣出鏡，做唔做到個人 IP？", "做到。腳本同分鏡由我哋寫，拍攝日有導演帶你講，一次半日拍晒成個月。未準備好出鏡，可以先用 AI 內容製作過渡。"),
            ("打造個人品牌要幾耐先見效？", "視乎行業同出片密度。我哋每月睇數據調整，你會見到觸及、留言同 WhatsApp 查詢點變化，再決定下一步。"),
        ],
        "related": ["video/", "social-media/"],
    },
    {
        "slug": "social-media/",
        "title": "IG代營運・Facebook專頁管理・Threads營運｜香港社交媒體代理｜JVM",
        "desc": "香港小店 IG 代營運、IG 代管、Facebook 專頁管理同 Threads 營運。按公式寫 post，你批咗先出，首月入門套餐 HK$3,000 起。",
        "eyebrow": "社交媒體代營運",
        "h1": "IG 代營運、Facebook 專頁管理、Threads 營運",
        "lede": "唔想請全職小編？JVM 做你嘅社交媒體代理：IG、Facebook、Threads 一齊打理，內容按痛點公式寫，每篇你批咗先出。",
        "blocks": [
            ("我哋負責乜", [
                ("Instagram 代管", "圖文、Reels、Story，回覆留言，留住有興趣嘅客。"),
                ("Facebook 專頁管理", "專頁資料、按鈕設定，內容同 IG 同步，唔使做兩次。"),
                ("Threads 營運", "老闆觀點短帖，同新客傾偈，再帶返去 IG。"),
            ]),
            ("每篇 post 都做齊 3 步", [
                ("頭 3 秒有痛點", "第一句講中客人嘅問題，啱嘅人先會停低。"),
                ("有嘢值得儲", "懶人包、清單，被儲低嘅 post 先會推俾非粉絲。"),
                ("結尾有留言 CTA", "留言多，IG 觸及率先會擴大。"),
            ]),
        ],
        "faq": [
            ("IG 代營運幾錢？", "JVM 首月入門套餐 HK$3,000 起，包 IG 診斷、內容系統同首月圖文。第二個月開始按你需要報價，廣告費另計。"),
            ("IG 冇人睇、觸及率低點算？", "多數係頭 3 秒冇痛點、冇嘢值得儲、冇留言 CTA。我哋免費幫你睇一次，話你知卡喺邊一步。"),
            ("你哋係咪會用我個帳號自動出 post？", "每篇內容你批咗先會發，唔啱可以叫我哋改，冇你同意唔會出。"),
        ],
        "related": ["meta-ads/", "ip/"],
    },
    {
        "slug": "video/",
        "title": "短片拍攝香港・Reels 拍攝・AI 影片製作｜真人上門拍片同 AI 內容｜JVM",
        "desc": "JVM 提供兩種內容製作：真人團隊上門拍片（Reels、宣傳短片、老闆出鏡），同 AI 內容製作（AI 圖文、AI 短片、廣東話 AI 短劇）。",
        "eyebrow": "內容製作",
        "h1": "短片拍攝同 AI 內容製作：兩條路，分開揀",
        "lede": "JVM 嘅內容製作分兩種：真人團隊落區上門拍片，同 AI 內容製作。你可以揀一種，亦可以兩種一齊用。",
        "blocks": [
            ("A・真人團隊上門拍片", [
                ("腳本分鏡", "我哋寫好每條 Reels 嘅腳本，你確認先拍。"),
                ("每月拍攝日", "攝影師同導演帶齊器材上門，半日拍晒成個月。"),
                ("後期製作", "剪接、廣東話字幕、配樂全包。"),
            ]),
            ("B・AI 內容製作", [
                ("AI 圖文", "IG post 同圖卡，唔使拍攝都有內容。"),
                ("AI 短片", "將現有素材剪成多條 Reels。"),
                ("廣東話 AI 短劇", "有角色、有對白，30 秒講晒你間舖嘅故事。"),
            ]),
        ],
        "faq": [
            ("真人拍片同 AI 短片有咩分別？", "真人拍片最有說服力，適合做老闆個人 IP；AI 內容快同多，適合未準備好出鏡或者喺拍攝日之間補內容。"),
            ("上門拍片要預幾耐時間？", "一般每月一個拍攝日，大約半日，一次過拍晒成個月要用嘅片。"),
            ("AI 短劇係咩？", "用 AI 製作嘅廣東話短劇，有角色同對白，約 30 秒，用故事帶出你間舖，比硬銷廣告易睇到尾。"),
        ],
        "related": ["ip/", "social-media/"],
    },
    {
        "slug": "google-maps/",
        "title": "Google商家檔案設定・Google Map排名優化｜香港本地SEO｜JVM",
        "desc": "幫香港小店設定同管理 Google 商家檔案（前稱 Google 我的商家），提升 Google Map 排名：資料、相片、更新、評價邀請同回覆。",
        "eyebrow": "Google 地圖・本地 SEO",
        "h1": "Google 商家檔案管理，令人搜「附近」見到你",
        "lede": "客人喺 Google 地圖搜「附近」「推介」，排前嘅多數資料齊、相多、評價多。JVM 幫你將 Google 商家檔案（前稱 Google 我的商家）一樣樣做好，做好本地 SEO。",
        "blocks": [
            ("我哋負責乜", [
                ("設定同驗證", "商家名稱、分類、營業時間、服務範圍，全部填齊。"),
                ("定期更新", "上載相片、發佈最新消息同優惠。"),
                ("評價管理", "邀請客人留 Google 評價，代你禮貌回覆。"),
            ]),
            ("Google Map 排名睇乜", [
                ("相關度", "資料同客人搜嘅字有幾吻合。"),
                ("距離", "你間舖同搜尋嘅人有幾近。"),
                ("知名度", "評價數量、評分，同網上幾多地方提及你。"),
            ]),
        ],
        "faq": [
            ("Google 我的商家同 Google 商家檔案有咩分別？", "係同一樣嘢，Google 我的商家而家改名做 Google 商家檔案（Google Business Profile）。"),
            ("Google Map 排名點樣做前啲？", "資料要齊、分類要啱、定期上相同更新、多啲真實評價，同埋網站同各平台嘅名稱電話要一致。"),
            ("冇實體舖可唔可以開 Google 商家檔案？", "可以揀做服務範圍商家，唔使公開地址，照樣出現喺地圖搜尋。"),
        ],
        "related": ["ai-seo/", "meta-ads/"],
    },
    {
        "slug": "ai-seo/",
        "title": "AI SEO・AI 搜尋優化｜令 ChatGPT 同 Google AI 推薦你間舖｜JVM",
        "desc": "AI SEO（又叫 GEO 生成式引擎優化）：幫香港小店令 ChatGPT、Gemini、Google AI 摘要搵到同推薦你。結構化資料、一致商家資料、問答式內容。",
        "eyebrow": "AI SEO",
        "h1": "AI SEO：人問 ChatGPT 推介，都講到你",
        "lede": "越來越多人問 ChatGPT、Gemini、Google AI 摘要「邊間好」。AI 會揀資料清楚、多處提及、答到問題嘅舖頭。AI SEO（又叫 GEO、生成式引擎優化）就係幫你成為 AI 揀中嗰間。",
        "blocks": [
            ("我哋負責乜", [
                ("結構化資料", "網站加商家、服務、價錢、常見問題標記，AI 一睇就明。"),
                ("商家資料一致", "網站、Google 商家檔案、IG、Facebook 嘅名稱、電話、地址一致。"),
                ("問答式內容", "寫客人真係會問嘅問題同答案，AI 最易引用。"),
            ]),
            ("AI SEO 同傳統 SEO 嘅分別", [
                ("傳統 SEO", "爭 Google 搜尋結果第一頁排名。"),
                ("AI SEO", "爭 AI 答案入面被提及同推薦。"),
                ("兩樣一齊做", "基礎一樣：清楚、可信、多處提及。"),
            ]),
        ],
        "faq": [
            ("AI SEO 係咩？", "AI SEO 係令 ChatGPT、Gemini、Google AI 摘要呢類 AI 工具，喺回答客人問題時提及同推薦你間舖嘅優化工作，亦叫 GEO（生成式引擎優化）。"),
            ("點樣令 ChatGPT 推薦我間舖？", "網上要有清楚、一致、可信嘅資料：網站結構化資料、Google 商家檔案、真實評價，同埋答到客人問題嘅內容。"),
            ("小店需唔需要做 AI SEO？", "如果你嘅客會上網問「邊間好」，就值得做。基礎工作同 Google 地圖、網站 SEO 重疊，一齊做最慳力。"),
        ],
        "related": ["google-maps/", "social-media/"],
    },
    {
        "slug": "meta-ads/",
        "title": "Meta廣告投放・Facebook廣告・IG廣告代理｜香港小店｜JVM",
        "desc": "JVM 幫香港小店做 Meta 廣告投放（Facebook 廣告、IG 廣告）：揀受眾、出廣告圖片同短片、寫文案、每星期睇數調整。預算由你定，每筆你批先落。",
        "eyebrow": "Meta 廣告",
        "h1": "Facebook 同 IG 廣告投放，推俾啱嘅街坊",
        "lede": "好內容加少少廣告費，可以推俾你間舖附近、啱年齡、啱興趣嘅人。JVM 負責 Meta 廣告設定、廣告素材同每星期數據調整。",
        "blocks": [
            ("我哋負責乜", [
                ("受眾設定", "按地區、年齡、興趣揀人，唔浪費錢推俾唔會嚟嘅人。"),
                ("廣告素材", "廣告圖、短片同文案全包，用你自己嘅 IP 內容最有效。"),
                ("數據調整", "每星期睇成效，停走唔掂嘅廣告，加碼有效嘅。"),
            ]),
        ],
        "faq": [
            ("Meta 廣告最少要落幾多錢？", "預算由你定，可以由細額開始試。廣告費直接俾 Meta，唔包喺 JVM 服務費入面，每筆你批咗先會落。"),
            ("Facebook 廣告同 IG 廣告要分開做咩？", "唔使。Meta 廣告可以一次過投放去 Facebook 同 Instagram，我哋會睇邊個平台效果好啲再調整。"),
            ("冇內容可唔可以直接落廣告？", "可以，但效果通常差好多。我哋建議先有幾條好內容，再揀表現最好嗰條加廣告。"),
        ],
        "related": ["social-media/", "video/"],
    },
    {
        "slug": "industries/physio/",
        "title": "痛症治療中心宣傳・物理治療中心推廣｜IG 同 Google 地圖｜JVM",
        "desc": "JVM 幫痛症治療中心、物理治療、跌打推拿做網上宣傳：治療師個人 IP、IG 衛教短片、Google 商家檔案同評價管理。",
        "eyebrow": "行業：痛症治療",
        "h1": "痛症治療中心點樣做網上宣傳",
        "lede": "痛症客人揀治療師，最睇信任。JVM 幫痛症治療中心、物理治療同跌打推拿店，用治療師個人 IP 同衛教短片建立信任，再用 Google 地圖等附近有需要嘅人搵到你。",
        "blocks": [
            ("適合痛症治療嘅內容", [
                ("衛教短片", "腰痛、膊頭痛、膝頭痛點樣自己檢查，專業但講得明。"),
                ("治療師出鏡", "治療師講自己點睇個案，客人未嚟已經認得你。"),
                ("Google 評價", "痊癒客人嘅真實評價，係新客最大嘅定心丸。"),
            ]),
        ],
        "faq": [
            ("痛症治療中心點宣傳最有效？", "治療師出鏡講衛教內容建立信任，加上 Google 商家檔案同真實評價，等附近有需要嘅人搜得到。"),
            ("醫療相關內容有咩要小心？", "唔可以誇大療效或者保證效果。我哋寫內容會以衛教同經驗分享為主。"),
        ],
        "related": ["ip/", "google-maps/"],
    },
    {
        "slug": "industries/cafe/",
        "title": "咖啡店宣傳・Cafe IG・小食店推廣｜香港餐飲社交媒體｜JVM",
        "desc": "JVM 幫香港咖啡店、Cafe、小食店做 IG 同 Google 地圖宣傳：店主個人 IP、出品 Reels、Google 商家檔案相片同評價。",
        "eyebrow": "行業：咖啡小食店",
        "h1": "咖啡店同小食店點樣做 IG 宣傳",
        "lede": "香港 Cafe 同小食店多，客人憑咩記得你？JVM 幫你拍出人想專登去食嘅理由：店主嘅堅持、出品嘅過程、熟客嘅故事，再用 Google 地圖等行開附近嘅人搵到你。",
        "blocks": [
            ("適合咖啡小食店嘅內容", [
                ("出品過程 Reels", "沖咖啡、整小食嘅特寫，最易令人停低。"),
                ("店主故事", "點解開呢間舖、揀豆嘅堅持，客人記得人多過記得餐牌。"),
                ("Google 地圖相片", "門面、餐牌、環境相，搜「附近 cafe」時第一印象。"),
            ]),
        ],
        "faq": [
            ("Cafe IG 應該拍乜？", "出品過程、店主故事、熟客反應，同埋第一次嚟必叫嘅推介。"),
            ("小食店點樣令人專登去？", "要有一個令人記得嘅理由，例如招牌出品或者店主個性，再喺 IG 同 Google 地圖不斷講。"),
        ],
        "related": ["video/", "google-maps/"],
    },
    {
        "slug": "industries/salon/",
        "title": "髮型屋宣傳・Salon IG 推廣・髮型師個人品牌｜香港｜JVM",
        "desc": "JVM 幫香港髮型屋同髮型師做網上宣傳：髮型師個人品牌、前後對比 Reels、IG 經營、Google 評價管理，令客人指定搵返同一個髮型師。",
        "eyebrow": "行業：髮型屋",
        "h1": "髮型屋同髮型師點樣做 IG 宣傳",
        "lede": "客人揀髮型屋，其實係揀髮型師。JVM 幫髮型屋同髮型師建立個人品牌：用前後對比同風格作品，令客人指定搵返同一個人。",
        "blocks": [
            ("適合髮型屋嘅內容", [
                ("前後對比 Reels", "剪髮、染髮前後對比，最直接見到手勢。"),
                ("髮型師個人品牌", "每個髮型師有自己風格同專長，客人搵人唔搵舖。"),
                ("Google 評價", "邀請滿意客人留評價，提及髮型師名，新客更易揀。"),
            ]),
        ],
        "faq": [
            ("髮型屋 IG 應該拍乜？", "前後對比、髮型師風格、護髮小知識，同埋客人改造故事。"),
            ("髮型師點樣建立個人品牌？", "固定風格同專長、經常出鏡、用同一套語氣同客人溝通，等客人記得你個人。"),
        ],
        "related": ["ip/", "social-media/"],
    },
]

CSS = """
:root{--ink:#0d0d0c;--ink-2:#1b1b19;--paper:#f3f1ea;--paper-2:#e4e1d6;--hi:#e6ff00;--mute-ink:#a9a79e;--mute-paper:#5c5a52;--line:#33332f;
--f:"Noto Sans HK","PingFang HK","Microsoft JhengHei",sans-serif;--fl:"Archivo Black","Arial Black",sans-serif;--fm:"JetBrains Mono",ui-monospace,Menlo,monospace;color-scheme:dark}
*{box-sizing:border-box}
body{margin:0;background:var(--ink);color:var(--paper);font-family:var(--f);line-height:1.75;-webkit-font-smoothing:antialiased}
a{color:inherit}a:focus-visible{outline:3px solid var(--hi);outline-offset:3px}
.wrap{max-width:60rem;margin:0 auto;padding-inline:clamp(16px,5vw,40px)}
.nav{position:sticky;top:env(safe-area-inset-top,0px);z-index:5;background:var(--ink);border-bottom:1px solid var(--line)}
.nav .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;padding-block:12px}
.logo{font-family:var(--fl);font-size:1.3rem;text-decoration:none}
.btn{display:inline-flex;background:var(--hi);color:var(--ink);font-weight:700;text-decoration:none;padding:12px 20px;border-radius:999px}
.nav .btn{padding:8px 16px;font-size:.88rem}
.crumbs{font-family:var(--fm);font-size:.75rem;color:var(--mute-ink);padding-top:28px}
.crumbs a{text-decoration:none}.crumbs a:hover{color:var(--paper)}
header.top{padding-block:28px 56px}
.eyebrow{font-family:var(--fm);font-size:.78rem;letter-spacing:.14em;color:var(--mute-ink);margin:0 0 12px}
h1{font-weight:900;font-size:clamp(2rem,6vw,3.4rem);line-height:1.15;margin:0;text-wrap:balance}
.lede{font-size:1.08rem;color:var(--mute-ink);max-width:38em;margin:18px 0 28px}
section{padding-block:clamp(48px,7vw,80px)}
.paper{background:var(--paper);color:var(--ink)}
h2{font-weight:900;font-size:clamp(1.5rem,3.6vw,2.2rem);line-height:1.25;margin:0 0 24px;text-wrap:balance}
.cards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin-bottom:40px}
.cards:last-child{margin-bottom:0}
.cards>div{border:1px solid var(--paper-2);border-radius:14px;padding:20px;min-width:0;background:#fff8}
.cards b{display:block;font-weight:900;font-size:1.05rem}
.cards p{margin:6px 0 0;color:var(--mute-paper);font-size:.95rem}
.faq details{border-bottom:1px solid var(--line);padding:16px 0}
.faq summary{cursor:pointer;font-weight:900;font-size:1.05rem}
.faq p{color:var(--mute-ink);margin:8px 0 0}
.rel{display:flex;flex-wrap:wrap;gap:10px;margin-top:8px}
.rel a{border:1px solid var(--ink);border-radius:999px;padding:8px 16px;text-decoration:none;font-weight:700}
.cta{background:var(--hi);color:var(--ink)}
.cta .btn{background:var(--ink);color:var(--hi)}
.cta p{margin:0 0 20px}
footer{border-top:1px solid var(--line);padding-block:32px;font-size:.85rem;color:var(--mute-ink)}
footer nav{display:flex;flex-wrap:wrap;gap:8px 18px;margin-bottom:14px}
footer a{text-decoration:none}footer a:hover{color:var(--paper)}
@media (max-width:760px){.cards{grid-template-columns:1fr}}
"""


def esc(s):
    return html.escape(s, quote=True)


def footer_links(prefix):
    items = [("", "首頁")] + NAV + INDUSTRIES
    return "".join(f'<a href="{prefix}{href}">{esc(label)}</a>' for href, label in items)


def render(p):
    depth = p["slug"].count("/")
    prefix = "../" * depth
    url = BASE + p["slug"]
    label = p["eyebrow"]
    crumbs = [("首頁", BASE)]
    if p["slug"].startswith("industries/"):
        crumbs.append(("行業", None))
    crumbs.append((label, url))
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Service",
                "name": p["h1"],
                "description": p["desc"],
                "url": url,
                "areaServed": {"@type": "Place", "name": "香港"},
                "provider": {
                    "@type": "ProfessionalService",
                    "name": "Just Vibing Media",
                    "url": BASE,
                    "telephone": "+852 5993 2444",
                    "email": EMAIL,
                },
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                    for q, a in p["faq"]
                ],
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": i + 1, "name": n, **({"item": u} if u else {})}
                    for i, (n, u) in enumerate(crumbs)
                ],
            },
        ],
    }
    crumb_html = " / ".join(
        f'<a href="{prefix}">首頁</a>' if n == "首頁" else esc(n) for n, _ in crumbs
    )
    blocks = ""
    for heading, cards in p["blocks"]:
        cells = "".join(f"<div><b>{esc(t)}</b><p>{esc(d)}</p></div>" for t, d in cards)
        blocks += f"<h2>{esc(heading)}</h2>\n<div class=\"cards\">{cells}</div>\n"
    faq = "".join(
        f"<details{' open' if i == 0 else ''}><summary>{esc(q)}</summary><p>{esc(a)}</p></details>"
        for i, (q, a) in enumerate(p["faq"])
    )
    names = dict(NAV + INDUSTRIES)
    rel = "".join(f'<a href="{prefix}{r}">{esc(names[r])}</a>' for r in p["related"])
    return f"""<!doctype html>
<html lang="zh-HK">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{esc(p["title"])}</title>
<meta name="description" content="{esc(p["desc"])}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Just Vibing Media">
<meta property="og:title" content="{esc(p["title"])}">
<meta property="og:description" content="{esc(p["desc"])}">
<meta property="og:url" content="{url}">
<meta property="og:locale" content="zh_HK">
<meta property="og:image" content="{BASE}img/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" sizes="32x32" href="{prefix}img/favicon-32.png">
<link rel="apple-touch-icon" href="{prefix}img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+HK:wght@400;700;900&family=Archivo+Black&family=JetBrains+Mono:wght@500&display=swap">
<link rel="stylesheet" href="{prefix}assets/site.css">
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=1)}
</script>
</head>
<body>
<nav class="nav" aria-label="主選單"><div class="wrap"><a class="logo" href="{prefix}">JVM</a><a class="btn" href="{WA}" target="_blank" rel="noopener">WhatsApp 查詢</a></div></nav>
<main>
<header class="top"><div class="wrap">
<p class="crumbs">{crumb_html}</p>
<p class="eyebrow">{esc(p["eyebrow"])}</p>
<h1>{esc(p["h1"])}</h1>
<p class="lede">{esc(p["lede"])}</p>
<a class="btn" href="{WA}" target="_blank" rel="noopener">WhatsApp 免費諮詢 →</a>
</div></header>
<section class="paper"><div class="wrap">
{blocks}<h2>相關服務</h2>
<div class="rel">{rel}<a href="{prefix}#pricing">收費：首月 HK$3,000 起</a></div>
</div></section>
<section><div class="wrap faq">
<h2>常見問題</h2>
{faq}
</div></section>
<section class="cta"><div class="wrap">
<h2>想知你間舖可以點做？</h2>
<p>WhatsApp 5993 2444 或 email {EMAIL}，講聲「診斷」，我哋免費幫你睇一次。</p>
<a class="btn" href="{WA}" target="_blank" rel="noopener">WhatsApp 我哋 →</a>
</div></section>
</main>
<footer><div class="wrap"><nav aria-label="全部服務">{footer_links(prefix)}</nav>
<span>© 2026 Just Vibing Media（JVM）· 香港 · WhatsApp 5993 2444 · {EMAIL}</span></div></footer>
</body>
</html>
"""


def main():
    os.makedirs("assets", exist_ok=True)
    with open("assets/site.css", "w") as f:
        f.write(CSS.strip() + "\n")
    for p in PAGES:
        os.makedirs(p["slug"], exist_ok=True)
        with open(os.path.join(p["slug"], "index.html"), "w") as f:
            f.write(render(p))
    urls = [BASE] + [BASE + p["slug"] for p in PAGES]
    body = "".join(f"  <url><loc>{u}</loc><lastmod>2026-10-09</lastmod></url>\n" for u in urls)
    with open("sitemap.xml", "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n'
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + body + "</urlset>\n")
    print(len(PAGES), "pages")


if __name__ == "__main__":
    main()
