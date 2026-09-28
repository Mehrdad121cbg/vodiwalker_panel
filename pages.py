# -*- coding: utf-8 -*-
# =====================================================================
#  VodiWalker — داشبورد «مرکز کنترل دیجیتال» (fa/en)
#  ✔ مطابق تصویر: سایدبار، کارت‌های آمار، نمودار ترافیک، پنل راست
#  ✔ بهینه برای موبایل و ویندوز (بدون backdrop-filter و بلور متحرک)
# =====================================================================
DASHBOARD_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl" data-lang="fa">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<title>VodiWalker | داشبورد</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;700;800;900&family=Inter:wght@400;500;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent}
:root{
 --bg:#08050f;--panel:rgba(255,255,255,.035);--panel2:rgba(255,255,255,.018);
 --line:rgba(255,255,255,.09);--line2:rgba(255,255,255,.16);
 --accent:#a855f7;--accent2:#7c3aed;--blue:#3ea6ff;--good:#22c55e;--warn:#f5a524;--bad:#f24955;
 --text:#f3f0fa;--sub:#9c93b5;--sub2:#655d7e;
 --sidebar-w:230px;--rail-w:296px;--top-h:62px;
}
html,body{height:100%}
body{background:var(--bg);color:var(--text);font-family:'Vazirmatn',sans-serif;font-size:14px;overflow:hidden;-webkit-font-smoothing:antialiased}
html[data-lang="en"] body{font-family:'Inter',sans-serif}
button{font-family:inherit;color:inherit;background:none;border:0;cursor:pointer}
input{font-family:inherit;color:inherit}
a{color:inherit;text-decoration:none}
::-webkit-scrollbar{width:7px;height:7px}
::-webkit-scrollbar-thumb{background:rgba(255,255,255,.12);border-radius:99px}
::-webkit-scrollbar-track{background:transparent}

/* پس‌زمینه کاملاً ایستا — بدون انیمیشن/بلور = صفر هزینه GPU */
.bg{position:fixed;inset:0;z-index:0;background:
 radial-gradient(45% 32% at 50% 0%,rgba(168,85,247,.15),transparent 60%),
 radial-gradient(38% 30% at 100% 100%,rgba(62,166,255,.07),transparent 60%),
 radial-gradient(30% 26% at 0% 90%,rgba(124,58,237,.10),transparent 60%),var(--bg)}

.app{position:relative;z-index:1;display:grid;height:100vh;height:100dvh;
 grid-template-columns:var(--sidebar-w) minmax(0,1fr);
 grid-template-rows:var(--top-h) minmax(0,1fr);
 grid-template-areas:"side top" "side content"}

/* ---------- سایدبار ---------- */
.sidebar{grid-area:side;display:flex;flex-direction:column;padding:16px 12px 12px;border-inline-end:1px solid var(--line);background:rgba(10,7,18,.72);overflow-y:auto}
.side-brand{display:flex;align-items:center;gap:10px;padding:4px 8px 16px}
.logo{width:38px;height:38px;flex:none;border-radius:12px;display:grid;place-items:center;background:linear-gradient(135deg,var(--accent2),var(--accent));color:#fff;font-size:19px;box-shadow:0 6px 18px rgba(124,58,237,.38)}
.side-brand b{display:block;font-size:14.5px;font-weight:900}
.side-brand small{display:block;font-size:8px;color:var(--sub);letter-spacing:.18em;font-weight:800;margin-top:2px}
.nav-label{font-size:9px;font-weight:800;letter-spacing:.16em;color:var(--sub2);padding:12px 10px 7px}
.nav-item{display:flex;align-items:center;gap:11px;padding:10px 12px;border-radius:12px;border:1px solid transparent;color:var(--sub);font-size:12.5px;font-weight:700;transition:color .15s,background-color .15s}
.nav-item i{font-size:17px;width:20px;text-align:center;flex:none}
.nav-item:hover{color:var(--text);background:rgba(255,255,255,.045)}
.nav-item.active{color:#fff;background:linear-gradient(90deg,rgba(124,58,237,.30),rgba(168,85,247,.08));border-color:rgba(168,85,247,.28)}
.n-badge{margin-inline-start:auto;font-size:9px;font-weight:800;padding:2px 7px;border-radius:99px;background:rgba(168,85,247,.16);color:#c9a8ff;border:1px solid rgba(168,85,247,.3)}
.n-badge.alert{background:rgba(242,73,85,.14);color:#ff9b9b;border-color:rgba(242,73,85,.3)}
.side-foot{margin-top:auto;display:flex;align-items:center;justify-content:space-between;padding:14px 10px 2px;border-top:1px dashed var(--line);font-size:10px;color:var(--sub)}
.side-status{display:flex;align-items:center;gap:7px;font-weight:800;color:var(--good)}

/* ---------- نوار بالا ---------- */
.topbar{grid-area:top;display:flex;align-items:center;gap:12px;padding:0 18px;border-bottom:1px solid var(--line);background:rgba(10,7,18,.6)}
.brand{display:none;align-items:center;gap:10px}
.brand-t b{display:block;font-size:14px;font-weight:900}
.brand-t small{display:block;font-size:8px;color:var(--sub);letter-spacing:.18em;font-weight:800}
.icon-btn{position:relative;width:38px;height:38px;flex:none;border-radius:12px;border:1px solid var(--line);background:rgba(255,255,255,.04);display:grid;place-items:center;color:var(--sub);font-size:16px;transition:color .15s,border-color .15s}
.icon-btn:hover{color:var(--text);border-color:var(--line2)}
.ndot{position:absolute;top:7px;inset-inline-end:7px;width:7px;height:7px;border-radius:50%;background:var(--bad);border:2px solid var(--bg)}
.searchbox{display:flex;align-items:center;gap:9px;flex:1;max-width:430px;background:rgba(0,0,0,.30);border:1px solid var(--line);border-radius:12px;padding:9px 13px;color:var(--sub)}
.searchbox input{flex:1;min-width:0;background:none;border:0;outline:0;font-size:12.5px}
.searchbox input::placeholder{color:var(--sub2)}
.top-actions{margin-inline-start:auto;display:flex;align-items:center;gap:10px}
.clock{font-size:11px;font-weight:700;color:var(--sub);white-space:nowrap}
.lang-switch{display:flex;background:rgba(255,255,255,.05);border:1px solid var(--line);border-radius:100px;padding:3px;gap:2px}
.lang-switch button{padding:5px 12px;border-radius:100px;color:var(--sub);font-size:11px;font-weight:700;transition:background-color .15s,color .15s}
.lang-switch button.on{background:linear-gradient(90deg,var(--accent2),var(--accent));color:#fff}
.avatar{width:38px;height:38px;flex:none;border-radius:12px;display:grid;place-items:center;font-size:11px;font-weight:900;color:#fff;background:linear-gradient(135deg,var(--accent),#6425d6)}

/* ---------- محتوا ---------- */
.content{grid-area:content;display:grid;grid-template-columns:minmax(0,1fr) var(--rail-w);min-height:0;min-width:0}
.main,.rail{overflow-y:auto;padding:18px;display:flex;flex-direction:column;gap:14px;-webkit-overflow-scrolling:touch}
.rail{border-inline-start:1px solid var(--line)}
.page-head{display:flex;align-items:flex-end;justify-content:space-between;gap:10px;flex-wrap:wrap}
.page-head h2{font-size:19px;font-weight:900}
.page-head p{font-size:11px;color:var(--sub);margin-top:4px}
.chip-live{display:inline-flex;align-items:center;gap:7px;padding:7px 12px;border-radius:99px;border:1px solid rgba(34,197,94,.25);background:rgba(34,197,94,.08);color:#7cf0a8;font-size:10px;font-weight:800}
.live-dot{width:7px;height:7px;border-radius:50%;background:var(--good);animation:pulse 1.8s ease-in-out infinite}
@keyframes pulse{50%{opacity:.35;transform:scale(.75)}}

/* ---------- کارت‌های آمار ---------- */
.stats-row{display:grid;grid-template-columns:repeat(auto-fit,minmax(155px,1fr));gap:12px}
.stat{padding:15px;border:1px solid var(--line);border-radius:16px;background:linear-gradient(160deg,var(--panel),var(--panel2));contain:layout style}
.stat-top{display:flex;align-items:center;justify-content:space-between;margin-bottom:11px}
.stat-ic{width:36px;height:36px;border-radius:11px;display:grid;place-items:center;font-size:17px;flex:none}
.stat-ic.p{background:rgba(168,85,247,.14);color:#c9a8ff}
.stat-ic.b{background:rgba(62,166,255,.12);color:#8fd9ff}
.stat-ic.g{background:rgba(34,197,94,.12);color:#7cf0a8}
.stat-ic.w{background:rgba(245,165,36,.13);color:#ffd28a}
.stat-val{font-size:21px;font-weight:900;letter-spacing:-.02em}
.stat-name{font-size:10.5px;font-weight:700;color:var(--sub);margin-top:3px}
.delta{display:inline-flex;align-items:center;gap:4px;font-size:9.5px;font-weight:800}
.delta i{font-size:12px}
.delta.up{color:#7cf0a8}
.delta.down{color:#8fd9ff}
.bar{height:5px;border-radius:99px;background:rgba(255,255,255,.07);margin-top:12px;overflow:hidden}
.bar>span{display:block;height:100%;border-radius:inherit;background:linear-gradient(90deg,var(--accent2),var(--accent));transform-origin:left center}
html[dir="rtl"] .bar>span{transform-origin:right center}
body.anim .bar>span{transition:transform .5s ease}

/* ---------- پنل‌ها ---------- */
.panel{border:1px solid var(--line);border-radius:18px;background:linear-gradient(160deg,var(--panel),var(--panel2));padding:17px;contain:layout style}
.panel-head{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-bottom:14px}
.panel-head h3{display:flex;align-items:center;gap:8px;font-size:13.5px;font-weight:800}
.panel-head h3 i{color:var(--accent);font-size:16px}
.legend{display:flex;gap:12px;font-size:10px;font-weight:800;color:var(--sub)}
.legend i{display:inline-block;width:9px;height:9px;border-radius:3px;margin-inline-end:5px;vertical-align:-1px}

/* ---------- نمودار ---------- */
.chart-wrap{position:relative;height:230px}
#netChart{display:block;width:100%;height:100%}

/* ---------- اتصال‌ها ---------- */
.conn-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(165px,1fr));gap:10px}
.conn{display:flex;align-items:center;gap:11px;padding:12px 13px;border:1px solid var(--line);border-radius:14px;background:var(--panel2)}
.conn-ic{width:34px;height:34px;border-radius:10px;display:grid;place-items:center;font-size:15px;flex:none}
.conn-ic.p{background:rgba(168,85,247,.14);color:#c9a8ff}
.conn-ic.b{background:rgba(62,166,255,.12);color:#8fd9ff}
.conn-ic.g{background:rgba(34,197,94,.12);color:#7cf0a8}
.conn-ic.w{background:rgba(245,165,36,.13);color:#ffd28a}
.conn b{display:block;font-size:16px;font-weight:900}
.conn small{font-size:9.5px;font-weight:700;color:var(--sub)}

/* ---------- فعالیت لحظه‌ای ---------- */
.act-list{display:flex;flex-direction:column;gap:8px}
.act-item{display:flex;gap:10px;padding:10px 11px;border:1px solid var(--line);border-radius:13px;background:var(--panel2)}
.act-item.new{animation:actIn .3s ease both}
@keyframes actIn{from{opacity:0;transform:translateY(-6px)}to{opacity:1;transform:none}}
.act-ic{width:30px;height:30px;flex:none;border-radius:9px;display:grid;place-items:center;font-size:14px}
.act-ic.p{background:rgba(168,85,247,.14);color:#c9a8ff}
.act-ic.g{background:rgba(34,197,94,.12);color:#7cf0a8}
.act-ic.b{background:rgba(62,166,255,.12);color:#8fd9ff}
.act-ic.w{background:rgba(245,165,36,.13);color:#ffd28a}
.act-t{font-size:11px;font-weight:700;line-height:1.7}
.act-m{font-size:9.5px;color:var(--sub2);margin-top:2px}

/* ---------- اقدامات سریع ---------- */
.quick-grid{display:grid;grid-template-columns:1fr 1fr;gap:9px}
.qa-btn{display:flex;flex-direction:column;align-items:center;gap:7px;padding:13px 8px;border:1px solid var(--line);border-radius:14px;background:var(--panel2);font-size:10px;font-weight:700;color:var(--sub);transition:color .15s,border-color .15s,transform .15s}
.qa-btn:hover{color:var(--text);border-color:var(--line2);transform:translateY(-1px)}
.qa-btn i{font-size:19px;color:var(--accent)}

/* ---------- سلامت سرور ---------- */
.gauge-wrap{position:relative;width:146px;margin:2px auto 8px}
.gauge{display:block;width:100%;transform:rotate(-90deg)}
.g-bg,.g-val{fill:none;stroke-width:9;stroke-linecap:round}
.g-bg{stroke:rgba(255,255,255,.07)}
.g-val{stroke:url(#gg);stroke-dasharray:314.16;stroke-dashoffset:6.3}
body.anim .g-val{transition:stroke-dashoffset .8s ease}
.gauge-center{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px}
.gauge-center b{font-size:22px;font-weight:900}
.gauge-center span{font-size:9px;font-weight:800;color:var(--good)}
.h-row{display:flex;align-items:center;gap:10px;margin-top:9px;font-size:10.5px}
.h-row>span{width:62px;flex:none;font-weight:700;color:var(--sub)}
.h-row .bar{flex:1;margin-top:0}
.h-row>b{width:42px;flex:none;text-align:end;font-size:10.5px}
.health-note{display:flex;align-items:center;gap:7px;margin-top:13px;padding:9px 11px;border-radius:11px;background:rgba(34,197,94,.07);border:1px solid rgba(34,197,94,.2);color:#7cf0a8;font-size:10px;font-weight:700}
.health-note i{font-size:14px;flex:none}

/* ---------- Toast ---------- */
.toast{position:fixed;bottom:18px;inset-inline-end:18px;z-index:99;display:flex;align-items:center;gap:9px;padding:12px 16px;border-radius:13px;background:#17102a;border:1px solid var(--line2);box-shadow:0 16px 40px rgba(0,0,0,.5);font-size:12px;font-weight:700;opacity:0;transform:translateY(10px);transition:opacity .25s ease,transform .25s ease;pointer-events:none}
.toast.show{opacity:1;transform:none}
.toast i{color:var(--good);font-size:16px}

/* ---------- موبایل ---------- */
.scrim{position:fixed;inset:0;z-index:39;background:rgba(4,2,10,.62);opacity:0;pointer-events:none;transition:opacity .2s ease}
.scrim.show{opacity:1;pointer-events:auto}
.menu-btn{display:none}
@media(max-width:1180px){
 .content{display:flex;flex-direction:column;overflow-y:auto}
 .main,.rail{overflow:visible}
 .rail{border-inline-start:0;border-top:1px solid var(--line)}
}
@media(max-width:860px){
 .app{grid-template-columns:minmax(0,1fr);grid-template-areas:"top" "content"}
 .sidebar{position:fixed;top:0;bottom:0;inset-inline-start:0;width:min(80vw,272px);z-index:40;transform:translateX(105%);transition:transform .26s ease}
 html[dir="ltr"] .sidebar{transform:translateX(-105%)}
 .sidebar.open{transform:translateX(0)!important}
 .menu-btn{display:grid}
 .brand{display:flex}
 .searchbox{display:none}
 .clock{display:none}
 .chart-wrap{height:175px}
}
@media(max-width:420px){
 .quick-grid{grid-template-columns:1fr}
 .page-head h2{font-size:16px}
}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
</style>
</head>
<body>
<div class="bg"></div>
<div class="app">

 <!-- ===== سایدبار ===== -->
 <aside class="sidebar" id="sidebar">
  <div class="side-brand">
   <div class="logo"><i class="ti ti-walk"></i></div>
   <div><b>VodiWalker</b><small data-i18n="tagline">مرکز کنترل دیجیتال</small></div>
  </div>
  <div class="nav-label" data-i18n="nav_main">اصلی</div>
  <a class="nav-item active" href="javascript:void(0)"><i class="ti ti-dashboard"></i><span data-i18n="nav_dash">داشبورد</span></a>
  <a class="nav-item" href="javascript:void(0)"><i class="ti ti-box"></i><span data-i18n="nav_inst">نمونه‌ها</span><span class="n-badge" id="nInst">1</span></a>
  <a class="nav-item" href="javascript:void(0)"><i class="ti ti-network"></i><span data-i18n="nav_net">شبکه</span></a>
  <a class="nav-item" href="javascript:void(0)"><i class="ti ti-database"></i><span data-i18n="nav_store">ذخیره‌سازی</span></a>
  <a class="nav-item" href="javascript:void(0)"><i class="ti ti-shield-lock"></i><span data-i18n="nav_sec">امنیت</span><span class="n-badge alert">3</span></a>
  <div class="nav-label" data-i18n="nav_sys">سیستم</div>
  <a class="nav-item" href="javascript:void(0)"><i class="ti ti-chart-bar"></i><span data-i18n="nav_ana">تحلیل‌ها</span></a>
  <a class="nav-item" href="javascript:void(0)"><i class="ti ti-file-text"></i><span data-i18n="nav_logs">گزارش رخدادها</span></a>
  <a class="nav-item" href="javascript:void(0)"><i class="ti ti-settings"></i><span data-i18n="nav_set">تنظیمات</span></a>
  <div class="side-foot">
   <span class="side-status"><span class="live-dot"></span><span data-i18n="online">آنلاین</span></span>
   <small data-i18n="ver">نسخه ۲.۱.۰</small>
  </div>
 </aside>
 <div class="scrim" id="scrim"></div>

 <!-- ===== نوار بالا ===== -->
 <header class="topbar">
  <button class="icon-btn menu-btn" id="menuBtn" aria-label="Menu"><i class="ti ti-menu-2"></i></button>
  <div class="brand">
   <div class="logo"><i class="ti ti-walk"></i></div>
   <div class="brand-t"><b>VodiWalker</b><small data-i18n="tagline">مرکز کنترل دیجیتال</small></div>
  </div>
  <div class="searchbox"><i class="ti ti-search"></i><input type="text" data-i18n-ph="search_ph" placeholder="جستجو در سیستم…"></div>
  <div class="top-actions">
   <span class="clock" id="clock"></span>
   <div class="lang-switch">
    <button id="langFa" class="on">فارسی</button>
    <button id="langEn">EN</button>
   </div>
   <button class="icon-btn" id="bellBtn" aria-label="Notifications"><i class="ti ti-bell"></i><span class="ndot"></span></button>
   <div class="avatar">AD</div>
  </div>
 </header>

 <!-- ===== محتوا ===== -->
 <div class="content">
  <main class="main">
   <div class="page-head">
    <div><h2 data-i18n="nav_dash">داشبورد</h2><p data-i18n="page_sub">نمای کلی وضعیت زیرساخت به‌صورت زنده</p></div>
    <span class="chip-live"><span class="live-dot"></span><span data-i18n="live">زنده</span></span>
   </div>

   <section class="stats-row">
    <div class="stat">
     <div class="stat-top"><div class="stat-ic p"><i class="ti ti-box"></i></div><span class="delta up"><i class="ti ti-circle-check"></i><span data-i18n="inst_run">در حال اجرا</span></span></div>
     <div class="stat-val" id="vInst">1</div>
     <div class="stat-name" data-i18n="stat_inst">کل نمونه‌ها</div>
    </div>
    <div class="stat">
     <div class="stat-top"><div class="stat-ic b"><i class="ti ti-database"></i></div><span class="delta up"><i class="ti ti-trending-up"></i>1.4%</span></div>
     <div class="stat-val" id="vStore">74%</div>
     <div class="stat-name" data-i18n="stat_store">مصرف ذخیره‌سازی</div>
     <div class="bar"><span id="bStore"></span></div>
    </div>
    <div class="stat">
     <div class="stat-top"><div class="stat-ic g"><i class="ti ti-network"></i></div><span class="delta down"><i class="ti ti-trending-down"></i>0.3%</span></div>
     <div class="stat-val" id="vNet">0.6%</div>
     <div class="stat-name" data-i18n="stat_net">ترافیک شبکه</div>
     <div class="bar"><span id="bNet"></span></div>
    </div>
    <div class="stat">
     <div class="stat-top"><div class="stat-ic w"><i class="ti ti-arrows-exchange"></i></div><span class="delta up"><i class="ti ti-trending-up"></i>3.2%</span></div>
     <div class="stat-val" id="vSwap">61.2%</div>
     <div class="stat-name" data-i18n="stat_swap">مصرف سواپ</div>
     <div class="bar"><span id="bSwap"></span></div>
    </div>
    <div class="stat">
     <div class="stat-top"><div class="stat-ic p"><i class="ti ti-cpu"></i></div><span class="delta down"><i class="ti ti-trending-down"></i>5.0%</span></div>
     <div class="stat-val" id="vCpu">19.1%</div>
     <div class="stat-name" data-i18n="stat_cpu">مصرف پردازنده</div>
     <div class="bar"><span id="bCpu"></span></div>
    </div>
   </section>

   <section class="panel">
    <div class="panel-head">
     <h3><i class="ti ti-chart-area"></i><span data-i18n="chart_title">جریان ترافیک شبکه</span></h3>
     <div class="legend">
      <span><i style="background:#a855f7"></i><span data-i18n="legend_in">دریافت</span></span>
      <span><i style="background:#3ea6ff"></i><span data-i18n="legend_out">ارسال</span></span>
     </div>
    </div>
    <div class="chart-wrap"><canvas id="netChart"></canvas></div>
   </section>

   <section class="panel">
    <div class="panel-head"><h3><i class="ti ti-plug-connected"></i><span data-i18n="conn_title">آمار اتصال‌ها</span></h3></div>
    <div class="conn-grid">
     <div class="conn"><div class="conn-ic b"><i class="ti ti-plug"></i></div><div><b id="vSock">29</b><small data-i18n="sockets">سوکت‌های باز</small></div></div>
     <div class="conn"><div class="conn-ic g"><i class="ti ti-link"></i></div><div><b id="vTcp">18</b><small data-i18n="tcp">اتصالات TCP فعال</small></div></div>
     <div class="conn"><div class="conn-ic p"><i class="ti ti-users"></i></div><div><b id="vUsers">4</b><small data-i18n="users">کاربران فعال</small></div></div>
     <div class="conn"><div class="conn-ic w"><i class="ti ti-clock-check"></i></div><div><b id="vUp">42d 13h</b><small data-i18n="uptime">مدت فعالیت</small></div></div>
    </div>
   </section>
  </main>

  <aside class="rail">
   <section class="panel">
    <div class="panel-head">
     <h3><i class="ti ti-activity"></i><span data-i18n="act_title">فعالیت لحظه‌ای</span></h3>
     <span class="chip-live"><span class="live-dot"></span><span data-i18n="live">زنده</span></span>
    </div>
    <div class="act-list" id="actList"></div>
   </section>

   <section class="panel">
    <div class="panel-head"><h3><i class="ti ti-bolt"></i><span data-i18n="qa_title">اقدامات سریع</span></h3></div>
    <div class="quick-grid">
     <button class="qa-btn" data-qa="t_ok_restart"><i class="ti ti-restart"></i><span data-i18n="qa_restart">ری‌استارت سرویس</span></button>
     <button class="qa-btn" data-qa="t_ok_cache"><i class="ti ti-trash"></i><span data-i18n="qa_cache">پاک‌سازی کش</span></button>
     <button class="qa-btn" data-qa="t_ok_backup"><i class="ti ti-cloud-upload"></i><span data-i18n="qa_backup">پشتیبان‌گیری</span></button>
     <button class="qa-btn" data-qa="t_ok_scan"><i class="ti ti-shield-lock"></i><span data-i18n="qa_scan">اسکن امنیتی</span></button>
    </div>
   </section>

   <section class="panel">
    <div class="panel-head"><h3><i class="ti ti-heartbeat"></i><span data-i18n="health_title">سلامت سرور</span></h3></div>
    <div class="gauge-wrap">
     <svg class="gauge" viewBox="0 0 120 120" aria-hidden="true">
      <defs><linearGradient id="gg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#22c55e"/><stop offset=".55" stop-color="#a855f7"/><stop offset="1" stop-color="#7c3aed"/></linearGradient></defs>
      <circle class="g-bg" cx="60" cy="60" r="50"/>
      <circle class="g-val" id="gaugeArc" cx="60" cy="60" r="50"/>
     </svg>
     <div class="gauge-center"><b id="vHealth">98%</b><span data-i18n="health_state">وضعیت عالی</span></div>
    </div>
    <div class="h-row"><span data-i18n="h_cpu">پردازنده</span><div class="bar"><span id="hCpu"></span></div><b id="tCpu">19.1%</b></div>
    <div class="h-row"><span data-i18n="h_ram">حافظه</span><div class="bar"><span id="hRam"></span></div><b id="tRam">57%</b></div>
    <div class="h-row"><span data-i18n="h_disk">دیسک</span><div class="bar"><span id="hDisk"></span></div><b id="tDisk">74%</b></div>
    <p class="health-note"><i class="ti ti-circle-check"></i><span data-i18n="health_note">همه سرویس‌ها پایدار و فعال هستند</span></p>
   </section>
  </aside>
 </div>
</div>

<div class="toast" id="toast"><i class="ti ti-circle-check"></i><span id="toastMsg"></span></div>

<script>
/* ================= ابزار ================= */
var FA_D='۰۱۲۳۴۵۶۷۸۹';
function $(id){return document.getElementById(id)}
function fmtNum(n){n=String(n);if(LANG!=='fa')return n;return n.replace(/\d/g,function(d){return FA_D[+d]}).replace('.','٫')}
function fmtPct(v){var s=(Math.round(v*10)%10===0)?String(Math.round(v)):v.toFixed(1);return LANG==='fa'?fmtNum(s)+'٪':s+'%'}

/* ================= متن‌های دوزبانه ================= */
var I18N={
fa:{tagline:'مرکز کنترل دیجیتال',search_ph:'جستجو در سیستم…',
 nav_main:'اصلی',nav_sys:'سیستم',nav_dash:'داشبورد',nav_inst:'نمونه‌ها',nav_net:'شبکه',nav_store:'ذخیره‌سازی',nav_sec:'امنیت',nav_ana:'تحلیل‌ها',nav_logs:'گزارش رخدادها',nav_set:'تنظیمات',
 online:'آنلاین',ver:'نسخه ۲.۱.۰',page_sub:'نمای کلی وضعیت زیرساخت به‌صورت زنده',live:'زنده',inst_run:'در حال اجرا',
 stat_inst:'کل نمونه‌ها',stat_store:'مصرف ذخیره‌سازی',stat_net:'ترافیک شبکه',stat_swap:'مصرف سواپ',stat_cpu:'مصرف پردازنده',
 chart_title:'جریان ترافیک شبکه',legend_in:'دریافت',legend_out:'ارسال',
 conn_title:'آمار اتصال‌ها',sockets:'سوکت‌های باز',tcp:'اتصالات TCP فعال',users:'کاربران فعال',uptime:'مدت فعالیت',
 act_title:'فعالیت لحظه‌ای',qa_title:'اقدامات سریع',qa_restart:'ری‌استارت سرویس',qa_cache:'پاک‌سازی کش',qa_backup:'پشتیبان‌گیری',qa_scan:'اسکن امنیتی',
 health_title:'سلامت سرور',health_state:'وضعیت عالی',h_cpu:'پردازنده',h_ram:'حافظه',h_disk:'دیسک',health_note:'همه سرویس‌ها پایدار و فعال هستند',
 t_ok_restart:'راه‌اندازی مجدد سرویس آغاز شد…',t_ok_cache:'حافظه نهان با موفقیت پاک شد',t_ok_backup:'فرایند پشتیبان‌گیری شروع شد',t_ok_scan:'اسکن امنیتی در حال اجراست',t_no_notif:'اعلان جدیدی وجود ندارد',
 just_now:'همین حالا',sec_ago:' ثانیه پیش',min_ago:' دقیقه پیش'},
en:{tagline:'DIGITAL CONTROL CENTER',search_ph:'Search the system…',
 nav_main:'MAIN',nav_sys:'SYSTEM',nav_dash:'Dashboard',nav_inst:'Instances',nav_net:'Network',nav_store:'Storage',nav_sec:'Security',nav_ana:'Analytics',nav_logs:'Logs',nav_set:'Settings',
 online:'Online',ver:'v2.1.0',page_sub:'Live overview of your infrastructure status',live:'LIVE',inst_run:'Running',
 stat_inst:'Total Instances',stat_store:'Storage Usage',stat_net:'Network Traffic',stat_swap:'Swap Usage',stat_cpu:'CPU Usage',
 chart_title:'Network Traffic Flow',legend_in:'Inbound',legend_out:'Outbound',
 conn_title:'Connection Statistics',sockets:'Open Sockets',tcp:'Active TCP',users:'Active Users',uptime:'Uptime',
 act_title:'Real-Time Activity',qa_title:'Quick Actions',qa_restart:'Restart Service',qa_cache:'Clear Cache',qa_backup:'Run Backup',qa_scan:'Security Scan',
 health_title:'Server Health',health_state:'Excellent',h_cpu:'CPU',h_ram:'RAM',h_disk:'Disk',health_note:'All services are stable and running',
 t_ok_restart:'Service restart initiated…',t_ok_cache:'Cache cleared successfully',t_ok_backup:'Backup process started',t_ok_scan:'Security scan running…',t_no_notif:'No new notifications',
 just_now:'just now',sec_ago:'s ago',min_ago:'m ago'}
};

var LANG='fa';
try{var _sl=localStorage.getItem('vw_lang');if(_sl==='fa'||_sl==='en')LANG=_sl}catch(e){}
function saveLang(l){try{localStorage.setItem('vw_lang',l)}catch(e){}}

function applyI18n(){
 var t=I18N[LANG],els=document.querySelectorAll('[data-i18n]'),i;
 for(i=0;i<els.length;i++){var k=els[i].getAttribute('data-i18n');if(t[k]!=null)els[i].textContent=t[k]}
 var ph=document.querySelectorAll('[data-i18n-ph]');
 for(i=0;i<ph.length;i++){var k2=ph[i].getAttribute('data-i18n-ph');if(t[k2]!=null)ph[i].placeholder=t[k2]}
}
function setLang(l){
 LANG=l;saveLang(l);
 $('langFa').className=l==='fa'?'on':'';$('langEn').className=l==='en'?'on':'';
 var r=document.documentElement;
 r.lang=l;r.dir=l==='fa'?'rtl':'ltr';r.setAttribute('data-lang',l);
 document.title='VodiWalker | '+(l==='fa'?'داشبورد':'Dashboard');
 applyI18n();renderStats();renderConn();renderGauge();renderAct();
 if(chart.ctx)chart.draw();
}

/* ================= داده‌ها (شبیه‌سازی — مقدار واقعی را اینجا بگذار) ================= */
var S={inst:1,store:74,net:0.6,swap:61.2,cpu:19.1,sockets:29,tcp:18,users:4,health:98,ram:57,disk:74,up:42*86400+13*3600+22*60};

function setBar(id,f){$(id).style.transform='scaleX('+Math.max(.02,Math.min(1,f))+')'}
function renderStats(){
 $('vInst').textContent=fmtNum(S.inst);$('nInst').textContent=fmtNum(S.inst);
 $('vStore').textContent=fmtPct(S.store);$('vNet').textContent=fmtPct(S.net);
 $('vSwap').textContent=fmtPct(S.swap);$('vCpu').textContent=fmtPct(S.cpu);
 setBar('bStore',S.store/100);setBar('bNet',S.net/100);setBar('bSwap',S.swap/100);setBar('bCpu',S.cpu/100);
}
function fmtUp(s){var d=Math.floor(s/86400),h=Math.floor(s%86400/3600);
 return LANG==='fa'?(fmtNum(d)+' روز و '+fmtNum(h)+' ساعت'):(d+'d '+h+'h')}
function renderConn(){
 $('vSock').textContent=fmtNum(S.sockets);$('vTcp').textContent=fmtNum(S.tcp);
 $('vUsers').textContent=fmtNum(S.users);$('vUp').textContent=fmtUp(S.up);
}
function renderGauge(){
 var C=2*Math.PI*50;
 $('gaugeArc').style.strokeDashoffset=(C*(1-S.health/100)).toFixed(2);
 $('vHealth').textContent=fmtPct(S.health);
 setBar('hCpu',S.cpu/100);setBar('hRam',S.ram/100);setBar('hDisk',S.disk/100);
 $('tCpu').textContent=fmtPct(S.cpu);$('tRam').textContent=fmtPct(S.ram);$('tDisk').textContent=fmtPct(S.disk);
}

/* ================= فعالیت لحظه‌ای ================= */
var ACT_TPL=[
 {i:'ti-server-2',c:'p',fa:'نمونه «web-0{n}» با موفقیت مستقر شد',en:'Instance "web-0{n}" deployed successfully'},
 {i:'ti-shield-check',c:'g',fa:'قوانین فایروال بروزرسانی شد',en:'Firewall rules updated'},
 {i:'ti-certificate',c:'b',fa:'گواهی SSL تمدید شد',en:'SSL certificate renewed'},
 {i:'ti-database',c:'w',fa:'پشتیبان‌گیری خودکار کامل شد',en:'Automated backup completed'},
 {i:'ti-cpu',c:'p',fa:'بار پردازنده مجدداً متوازن شد',en:'CPU load rebalanced'},
 {i:'ti-user-check',c:'g',fa:'ورود مدیر تأیید شد',en:'Admin login verified'},
 {i:'ti-network',c:'b',fa:'گیت‌وی شبکه پایدار است',en:'Network gateway stable'},
 {i:'ti-alert-triangle',c:'w',fa:'هشدار جزئی: مصرف سواپ در حال افزایش',en:'Minor alert: rising swap usage'}
];
var actItems=[];
function addAct(ageMs){
 var t=ACT_TPL[Math.floor(Math.random()*ACT_TPL.length)];
 actItems.unshift({i:t.i,c:t.c,fa:t.fa,en:t.en,ts:Date.now()-(ageMs||0)});
 if(actItems.length>7)actItems.pop();
 renderAct();
}
function fmtAgo(ts){
 var s=Math.floor((Date.now()-ts)/1000),t=I18N[LANG];
 if(s<12)return t.just_now;
 if(s<60)return fmtNum(s)+t.sec_ago;
 return fmtNum(Math.floor(s/60))+t.min_ago;
}
function renderAct(){
 var h='',k;
 for(k=0;k<actItems.length;k++){
  var a=actItems[k],txt=(LANG==='fa'?a.fa:a.en).replace('{n}',String(1+Math.floor(Math.random()*3)));
  h+='<div class="act-item'+(k===0?' new':'')+'"><div class="act-ic '+a.c+'"><i class="ti '+a.i+'"></i></div><div style="flex:1;min-width:0"><div class="act-t">'+txt+'</div><div class="act-m">'+fmtAgo(a.ts)+'</div></div></div>';
 }
 $('actList').innerHTML=h;
}

/* ================= نمودار (Canvas سبک — بدون کتابخانه) ================= */
var chart={
 cv:null,ctx:null,w:0,h:0,cap:44,data:[],
 init:function(){
  this.cv=$('netChart');this.ctx=this.cv.getContext('2d');
  var v=0.6;
  for(var k=0;k<this.cap;k++){
   v=Math.max(.1,Math.min(2,v+(Math.random()-.5)*.22));
   this.data.push({i:v,o:Math.max(.05,v*(.45+Math.random()*.3))});
  }
  this.resize(true);
 },
 resize:function(skipDraw){
  var r=this.cv.parentNode.getBoundingClientRect();
  var dpr=Math.min(window.devicePixelRatio||1,2); /* سقف DPR=2 برای کارایی */
  this.w=Math.max(60,r.width);this.h=Math.max(80,r.height);
  this.cv.width=Math.round(this.w*dpr);this.cv.height=Math.round(this.h*dpr);
  this.ctx.setTransform(dpr,0,0,dpr,0,0);
  if(!skipDraw)this.draw();
 },
 push:function(v){
  this.data.push({i:v,o:Math.max(.05,v*(.45+Math.random()*.3))});
  if(this.data.length>this.cap)this.data.shift();
  this.draw();
 },
 draw:function(){
  var c=this.ctx,W=this.w,H=this.h;if(!W||!H)return;
  c.clearRect(0,0,W,H);
  c.strokeStyle='rgba(255,255,255,.055)';c.lineWidth=1;
  for(var g=1;g<4;g++){var y=Math.round(H/4*g)+.5;c.beginPath();c.moveTo(0,y);c.lineTo(W,y);c.stroke();}
  var mx=.5,k;
  for(k=0;k<this.data.length;k++){if(this.data[k].i>mx)mx=this.data[k].i;if(this.data[k].o>mx)mx=this.data[k].o;}
  mx=Math.ceil(mx*1.2*10)/10;
  this.series(this.data.map(function(p){return p.i}),'#a855f7','168,85,247',mx);
  this.series(this.data.map(function(p){return p.o}),'#3ea6ff','62,166,255',mx);
  c.fillStyle='rgba(156,147,181,.85)';c.font='700 9px Inter, Vazirmatn, sans-serif';
  c.textAlign='left';c.textBaseline='alphabetic';
  c.fillText(fmtNum(mx.toFixed(1))+(LANG==='fa'?'٪':'%'),6,14);
  c.fillText('0',6,H-6);
 },
 series:function(vals,color,rgb,mx){
  var c=this.ctx,W=this.w,H=this.h,n=vals.length;
  if(n<2)return;
  var step=W/(this.cap-1),x0=W-(n-1)*step,pad=12;
  function X(i){return x0+i*step}
  function Y(v){return H-pad-(v/mx)*(H-2*pad)}
  var pts=[],i;
  for(i=0;i<n;i++)pts.push([X(i),Y(vals[i])]);
  function path(close){
   c.beginPath();c.moveTo(pts[0][0],pts[0][1]);
   for(var j=1;j<n;j++){var xc=(pts[j-1][0]+pts[j][0])/2,yc=(pts[j-1][1]+pts[j][1])/2;c.quadraticCurveTo(pts[j-1][0],pts[j-1][1],xc,yc);}
   c.lineTo(pts[n-1][0],pts[n-1][1]);
   if(close){c.lineTo(pts[n-1][0],H+2);c.lineTo(pts[0][0],H+2);c.closePath();}
  }
  path(true);
  var gr=c.createLinearGradient(0,0,0,H);
  gr.addColorStop(0,'rgba('+rgb+',.20)');gr.addColorStop(1,'rgba('+rgb+',0)');
  c.fillStyle=gr;c.fill();
  path(false);
  c.strokeStyle=color;c.lineWidth=2;c.lineJoin='round';c.lineCap='round';c.stroke();
  c.beginPath();c.arc(pts[n-1][0],pts[n-1][1],3,0,6.29);c.fillStyle=color;c.fill();
 }
};

/* ================= تیک‌های زمانی (توقف خودکار در تب مخفی) ================= */
var timers=[];
function startTimers(){stopTimers();
 timers.push(setInterval(dataTick,2000));
 timers.push(setInterval(function(){if(!document.hidden)addAct(0)},6500));
 timers.push(setInterval(clockTick,1000));
 timers.push(setInterval(function(){if(!document.hidden)renderAct()},10000));
}
function stopTimers(){for(var k=0;k<timers.length;k++)clearInterval(timers[k]);timers=[]}
function rnd(v,min,max,jit){return Math.max(min,Math.min(max,v+(Math.random()-.5)*jit))}
function dataTick(){
 S.store=rnd(S.store,55,95,1.6);S.net=rnd(S.net,.1,2.4,.3);
 S.swap=rnd(S.swap,40,80,1.4);S.cpu=rnd(S.cpu,8,70,4);
 S.sockets=Math.round(rnd(S.sockets,18,60,6));S.tcp=Math.round(rnd(S.tcp,10,40,4));
 S.users=Math.max(1,Math.round(rnd(S.users,1,12,1.5)));
 S.health=Math.round(rnd(S.health,90,100,1.5));S.ram=rnd(S.ram,45,75,2);
 S.up+=2;
 chart.push(S.net);
 renderStats();renderConn();renderGauge();
}
function clockTick(){
 if(document.hidden)return;
 try{$('clock').textContent=new Intl.DateTimeFormat(LANG==='fa'?'fa-IR':'en-US',{dateStyle:'medium',timeStyle:'short'}).format(new Date())}
 catch(e){$('clock').textContent=new Date().toLocaleString()}
}

/* ================= Toast و رویدادها ================= */
var toastT=null;
function toast(msg){
 $('toastMsg').textContent=msg;
 var t=$('toast');t.classList.add('show');
 clearTimeout(toastT);toastT=setTimeout(function(){t.classList.remove('show')},2200);
}
function openSidebar(){$('sidebar').classList.add('open');$('scrim').classList.add('show')}
function closeSidebar(){$('sidebar').classList.remove('open');$('scrim').classList.remove('show')}

 $('menuBtn').addEventListener('click',openSidebar);
 $('scrim').addEventListener('click',closeSidebar);
 $('langFa').addEventListener('click',function(){setLang('fa')});
 $('langEn').addEventListener('click',function(){setLang('en')});
 $('bellBtn').addEventListener('click',function(){toast(I18N[LANG].t_no_notif)});

var qas=document.querySelectorAll('.qa-btn');
for(var q=0;q<qas.length;q++)(function(b){b.addEventListener('click',function(){toast(I18N[LANG][b.getAttribute('data-qa')])})})(qas[q]);

var navs=document.querySelectorAll('.nav-item');
for(var nv=0;nv<navs.length;nv++)(function(el){el.addEventListener('click',function(){
 for(var j=0;j<navs.length;j++)navs[j].classList.remove('active');
 el.classList.add('active');closeSidebar();
})})(navs[nv]);

var rzT=null;
window.addEventListener('resize',function(){clearTimeout(rzT);rzT=setTimeout(function(){chart.resize(false)},160)},{passive:true});
document.addEventListener('visibilitychange',function(){if(document.hidden)stopTimers();else{startTimers();clockTick()}});

/* ================= شروع ================= */
chart.init();
addAct(141000);addAct(96000);addAct(47000);addAct(0);
setLang(LANG);
clockTick();
startTimers();
setTimeout(function(){document.body.classList.add('anim')},80);
</script>
</body>
</html>
"""
