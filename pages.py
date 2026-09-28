LOGIN_HTML = r"""<!DOCTYPE html>
<html lang="fa" dir="rtl" id="htmlRoot">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>VodiWalker | Login</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;500;600;700;800;900&family=Estedad:wght@400;500;600;700;800;900&family=IBM+Plex+Sans+Arabic:wght@400;500;600;700;800&family=Shabnam:wght@400;500;700&family=Yekan+Bakh:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/@tabler/icons-webfont@3.19.0/dist/tabler-icons.min.css">
<style>
*{margin:0;padding:0;box-sizing:border-box}
:root{
  --bg:#08050f;--panel:rgba(255,255,255,.035);--line:rgba(255,255,255,.09);--line2:rgba(255,255,255,.16);
  --accent:#a855f7;--accent2:#7c3aed;--accent3:#22c55e;
  --text:#f3f0fa;--sub:#9c93b5;--sub2:#655d7e;
  --font-fa:'Vazirmatn',sans-serif;--font-en:'Inter',sans-serif;
}
html,body{background:var(--bg);color:var(--text);min-height:100%;font-family:var(--font-fa)}
html[data-lang="en"] body{font-family:var(--font-en)}
a{color:inherit;text-decoration:none}
button{font-family:inherit;cursor:pointer}
body{
  min-height:100vh;min-height:100svh;min-height:100dvh;display:flex;align-items:center;justify-content:center;position:relative;overflow-x:hidden;overflow-y:auto;padding:24px;
  background:
    radial-gradient(48% 40% at 50% 8%, rgba(168,85,247,.30), transparent 60%),
    radial-gradient(40% 35% at 12% 85%, rgba(124,58,237,.22), transparent 60%),
    radial-gradient(40% 35% at 90% 80%, rgba(34,197,94,.10), transparent 60%),
    #08050f;
}
/* روی صفحات کوتاه (موبایل، زوم بالا، پنجره کوچک) اجازه می‌ده کاربر اسکرول کنه
   تا کل کارت (شامل دکمه‌ی «ثبت‌نام ادمینی» زیر کارت ورود) قابل دیدن و کلیک باشه؛
   وقتی محتوا داخل صفحه جا می‌شه ظاهر صفحه دقیقاً مثل قبل باقی می‌مونه. */
@media (max-height:760px){
  body{align-items:flex-start;padding-top:28px;padding-bottom:28px}
}
.grid-bg{position:absolute;inset:0;opacity:.35;background-image:linear-gradient(rgba(255,255,255,.045) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.045) 1px,transparent 1px);background-size:38px 38px;mask-image:radial-gradient(65% 55% at 50% 30%,#000 20%,transparent 85%)}
 .grid-bg:before{content:"";position:absolute;inset:-2%;background:conic-gradient(from 0deg,transparent 0deg,rgba(168,85,247,.12) 65deg,transparent 130deg,rgba(62,166,255,.10) 210deg,transparent 290deg);filter:blur(24px);animation:ambientSpin 18s linear infinite;will-change:transform;contain:strict}
@keyframes ambientSpin{to{transform:rotate(360deg)}}
.scanline{position:absolute;inset:0;pointer-events:none;background:linear-gradient(180deg,transparent 0%,rgba(255,255,255,.025) 48%,transparent 52%);background-size:100% 180px;animation:scan 7s linear infinite;mix-blend-mode:screen}
@keyframes scan{to{background-position:0 180px}}
.ambient-orb{position:absolute;border-radius:50%;filter:blur(2px);opacity:.45;animation:floatOrb 9s ease-in-out infinite}
.ambient-orb.a{width:180px;height:180px;right:9%;top:12%;background:radial-gradient(circle,rgba(168,85,247,.35),transparent 70%)}
.ambient-orb.b{width:240px;height:240px;left:3%;bottom:3%;background:radial-gradient(circle,rgba(62,166,255,.22),transparent 70%);animation-delay:-3s}
@keyframes floatOrb{0%,100%{transform:translate3d(0,0,0)}50%{transform:translate3d(0,-18px,0)}}
.dot{position:absolute;width:3px;height:3px;border-radius:50%;background:#c9a8ff;opacity:.6;animation:twinkle 3.4s ease-in-out infinite}
@keyframes twinkle{0%,100%{opacity:.15;transform:scale(1)}50%{opacity:.9;transform:scale(1.6)}}

.lang-switch{position:absolute;top:22px;left:22px;z-index:5;display:flex;background:rgba(255,255,255,.05);border:1px solid var(--line);border-radius:100px;padding:3px;gap:2px}
html[dir="rtl"] .lang-switch{left:auto;right:22px}
.lang-switch button{padding:6px 14px;border:0;background:transparent;color:var(--sub);font-size:12px;font-weight:700;border-radius:100px;transition:.15s}
.lang-switch button.on{background:linear-gradient(90deg,var(--accent2),var(--accent));color:#fff}

.wrap{position:relative;z-index:1;width:100%;max-width:420px;display:flex;flex-direction:column;align-items:center;animation:rise .55s cubic-bezier(.2,.8,.2,1) both}
.wrap{position:relative;z-index:1;width:100%;max-width:470px;display:flex;flex-direction:column;align-items:center;animation:rise .65s cubic-bezier(.2,.8,.2,1) both}
.login-status{display:flex;align-items:center;gap:8px;margin:0 0 12px;padding:7px 11px;border-radius:999px;border:1px solid rgba(62,166,255,.18);background:rgba(10,18,32,.58);box-shadow:0 8px 30px rgba(0,0,0,.18);font-size:9px;letter-spacing:.12em;color:#9ecfff;text-transform:uppercase}.login-status .live{width:7px;height:7px;border-radius:50%;background:#34d399;box-shadow:0 0 0 5px rgba(52,211,153,.08),0 0 14px rgba(52,211,153,.8);animation:statusPulse 1.8s ease-in-out infinite}@keyframes statusPulse{50%{transform:scale(1.25);opacity:.65}}
.security-strip{display:flex;justify-content:center;gap:7px;flex-wrap:wrap;margin-top:14px}.security-strip span{font-size:8.5px;color:var(--sub);padding:6px 8px;border:1px solid var(--line);border-radius:8px;background:rgba(255,255,255,.025)}.security-strip i{color:#8fd9ff;margin-left:3px}
.login-card-glow{position:absolute;inset:-1px;border-radius:23px;background:conic-gradient(from 180deg,rgba(168,85,247,.0),rgba(168,85,247,.55),rgba(62,166,255,.35),rgba(168,85,247,.0));filter:blur(8px);opacity:.18;z-index:-1;animation:cardGlow 8s linear infinite;will-change:transform;contain:strict}@keyframes cardGlow{to{transform:rotate(360deg)}}
@keyframes rise{from{opacity:0;transform:translateY(16px)}to{opacity:1;transform:translateY(0)}}

.badge-wrap{position:relative;width:92px;height:92px;margin:14px 0 30px}
.orbit-ring{position:absolute;inset:-24px;border-radius:50%;border:1px dashed rgba(168,85,247,.35);animation:orbitspin 7s linear infinite}
.orbit-ring2{position:absolute;inset:-38px;border-radius:50%;border:1px dashed rgba(62,166,255,.20);animation:orbitspin 12s linear infinite reverse}
.planet{position:absolute;top:-5px;left:50%;width:10px;height:10px;margin-left:-5px;border-radius:50%;background:radial-gradient(circle at 30% 30%,#c9f0ff,#3ea6ff 55%,#1c5fa8 100%);box-shadow:0 0 12px 2px rgba(62,166,255,.85)}
.planet2{position:absolute;bottom:-4px;left:50%;width:6px;height:6px;margin-left:-3px;border-radius:50%;background:radial-gradient(circle at 30% 30%,#f3d9ff,#a855f7 60%,#6425d6 100%);box-shadow:0 0 9px 2px rgba(168,85,247,.85)}
@keyframes orbitspin{to{transform:rotate(360deg)}}
.badge-glow{position:absolute;inset:-14px;border-radius:50%;background:radial-gradient(circle,rgba(168,85,247,.55),transparent 70%);filter:blur(6px);animation:pulseGlow 2.6s ease-in-out infinite;will-change:transform,opacity;contain:strict}
@keyframes pulseGlow{0%,100%{opacity:.6;transform:scale(1)}50%{opacity:1;transform:scale(1.08)}}
.badge{position:relative;width:92px;height:92px;border-radius:50%;overflow:hidden;border:2px solid rgba(255,255,255,.18);box-shadow:0 10px 40px -6px rgba(168,85,247,.7);background:#150c26;display:flex;align-items:center;justify-content:center}
.badge img{width:100%;height:100%;object-fit:cover}

.brand-caps{font-size:12px;font-weight:800;letter-spacing:.32em;color:#c9a8ff;margin-bottom:14px}
h1{font-size:29px;font-weight:900;text-align:center;line-height:1.5;color:var(--text)}
h1 .g{background:linear-gradient(90deg,#c9a8ff,#a855f7,#8fd9ff);-webkit-background-clip:text;background-clip:text;color:transparent}
.subtitle{margin-top:10px;font-size:13.5px;color:var(--sub);text-align:center;line-height:1.9;max-width:340px}

.card{position:relative;
  width:100%;margin-top:28px;padding:30px 28px;border-radius:24px;
  background:linear-gradient(180deg,rgba(255,255,255,.045),rgba(255,255,255,.015));
  border:1px solid var(--line);backdrop-filter:none;
  box-shadow:0 36px 100px -26px rgba(0,0,0,.62), inset 0 1px 0 rgba(255,255,255,.05);
}
.field{margin-bottom:16px}
.field label{display:block;font-size:12px;font-weight:700;color:var(--sub);margin-bottom:8px}
.inp{position:relative}
.inp input{width:100%;padding:14px 44px;border-radius:12px;border:1px solid var(--line);background:rgba(0,0,0,.28);color:var(--text);font-size:14px;outline:none;transition:.15s;font-family:inherit}
.inp input::placeholder{color:var(--sub2)}
.inp input:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(168,85,247,.20)}
.inp i.i-lead{position:absolute;right:14px;top:50%;transform:translateY(-50%);color:var(--sub);font-size:16px;pointer-events:none}
html[dir="ltr"] .inp i.i-lead{right:auto;left:14px}
html[dir="ltr"] .inp input{padding:13px 42px}
.toggle-eye{position:absolute;left:12px;top:50%;transform:translateY(-50%);background:none;border:0;color:var(--sub);font-size:16px;padding:4px;border-radius:6px;transition:.15s}
html[dir="ltr"] .toggle-eye{left:auto;right:12px}
.toggle-eye:hover{color:var(--text);background:rgba(255,255,255,.07)}
.remember{display:flex;align-items:center;gap:8px;font-size:12.5px;color:var(--sub);margin:2px 0 20px;user-select:none;cursor:pointer}
.remember input{accent-color:var(--accent);width:15px;height:15px}
.error{display:flex;gap:8px;align-items:center;background:rgba(239,68,68,.10);border:1px solid rgba(239,68,68,.30);color:#ff9b9b;border-radius:11px;padding:11px 13px;font-size:12.5px;margin-bottom:16px}
.error::before{content:"\ea87";font-family:"tabler-icons";font-size:15px;flex-shrink:0}
