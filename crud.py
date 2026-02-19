@import url('https://fonts.googleapis.com/css2?family=Inder&display=swap');

/* ===== Загальні стилі ===== */
* {
  box-sizing: border-box; 
  margin: 0;
  padding: 0;
}

html, body {
  height: 100%; 
}
body {
  font-family: 'Inder', sans-serif; 
  background: #111827; 
  padding: 24px; 
}

.app {
  background: #f3f4f6; 
  border-radius: 10px; 
  display: flex;       
  min-height: 90vh;   
  overflow: visible;    
  box-shadow: 0 20px 30px #0000004d; 
}

/* ===== SIDEBAR ===== */
aside {
  width: 220px;        
  background: #ffffff;  
  padding: 24px 16px;   
  box-shadow: 5px 0 20px rgba(0,0,0,0.15); 
  display: flex;        
  flex-direction: column; 
  gap: 24px;             
  position: relative;    /* щоб іконка профілю була відносно aside */
}

/* ===== Логотип ===== */
.logo {
  font-weight: 400;                 
  font-style: normal;               
  font-size: 35px;                  
  line-height: 1;                   
  letter-spacing: 0;                
  color: #111827;
}

/* ===== Посилання навігації ===== */
nav a {
  display: block; 
  padding: 8px 8px; 
  color: #6b7280; 
  text-decoration: none; 
  border-radius: 6px; 
  transition: 0.2s; 
}

nav a:hover {
  background: #f3f4f6; 
  text-decoration: underline; 
}

/* Активний пункт меню */
nav a.active {
  color: #190A7D; 
  font-weight: 600; 
  text-decoration: underline;
}

/* ===== Іконка профілю ===== */
.profile-icon {
  position: absolute; 
  bottom: 20px; 
  left: 20px;
  width: 48px;
  height: 48px;
  border-radius: 50%; 
  transition: 0.2s; 
}

.profile-icon img {
  width: 100%;
  height: 100%;
  object-fit: cover; 
}

/* ===== MAIN ===== */
main {
  flex: 1;
  padding: 32px;
  min-height: calc(90vh - 48px); 
  display: flex;
  flex-direction: column;
  overflow-y: auto;
}

/* ===== КАРТОЧКИ ===== */
.card {
  background: #ffffff;
  border-radius: 10px;
  padding: 24px; 
  margin-bottom: 24px; 
  box-shadow: 0 6px 18px #00000014; 
}

.card h2 {
  font-size: 18px;
  font-weight: 700;
  color: #111827;
  margin-bottom: 14px; 
}

.card hr {
  border: none;
  border-top: 1px solid #e5e7eb;
  margin: 12px 0;
}

/* Секції всередині карточки */
.section {
  margin-bottom: 12px; 
}

/* Підписи */
.label {
  font-weight: 600;
  margin-bottom: 4px;
  color: #111827;
}

/* Текст всередині секцій */
.section p,
.section div {
  margin-left: 0; 
  color: #000000; 
  font-weight: 400;
  line-height: 1.5;
}

