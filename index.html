<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PREDIX | Clinical Intelligence</title>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;800&display=swap" rel="stylesheet">
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        :root {
            --bg: #050505;
            --glass: rgba(18, 18, 18, 0.7);
            --border: rgba(255, 255, 255, 0.08);
            --accent: #ff3c3c;
            --text-main:#94a3b8 ;
            --text-dim: #94a3b8;
            --radius: 20px;
        }

        * { box-sizing: border-box; }

        body {
            margin: 0;
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: var(--bg);
            color: var(--text-main);
            background-image: 
                radial-gradient(circle at 50% -10%, #450a0a 0%, transparent 40%),
                radial-gradient(circle at 0% 100%, #1a0505 0%, transparent 30%);
            background-attachment: fixed;
        }

        /* CLEAN NAV */
        .navbar {
            padding: 25px 50px;
            display: flex;
            justify-content: center;
            border-bottom: 1px solid var(--border);
            backdrop-filter: blur(15px);
            position: sticky; top: 0; z-index: 1000;
        }
        .nav-logo { font-weight: 800; font-size: 26px; letter-spacing: -1.5px; color: var(--accent); }

        .container { max-width: 1300px; margin: 0 auto; padding: 60px 20px; }

        /* MINIMAL HERO SECTION */
        header { text-align: center; margin-bottom: 80px; }
        header h1 { 
            font-size: clamp(40px, 8vw, 82px); 
            font-weight: 800; 
            letter-spacing: -4px; 
            margin: 0; 
            background: linear-gradient(180deg, #fff 0%, #666 100%);
            -webkit-background-clip: text; 
            -webkit-text-fill-color: transparent; 
            line-height: 0.9;
        }
        header p { color: var(--text-dim); font-size: 18px; margin-top: 25px; max-width: 600px; margin-left: auto; margin-right: auto; opacity: 0.8; }

        /* BENTO STATS */
        .bento-grid {
            display: grid;
            grid-template-columns: repeat(12, 1fr);
            grid-auto-rows: 140px;
            gap: 16px;
            margin-bottom: 100px;
        }
        .bento-card {
            background: var(--glass);
            border: 1px solid var(--border);
            padding: 24px;
            border-radius: 24px;
            backdrop-filter: blur(10px);
            transition: transform 0.3s ease;
        }
        .bento-card:hover { transform: translateY(-5px); border-color: var(--accent); }
        .bento-card h4 { font-size: 11px; text-transform: uppercase; color: var(--text-dim); margin: 0; letter-spacing: 1px; }
        .bento-card .stat { font-size: 38px; font-weight: 700; color: var(--accent); margin: 10px 0; }
        .span-8 { grid-column: span 8; }
        .span-4 { grid-column: span 4; }
        .span-6 { grid-column: span 6; }
        .row-2 { grid-row: span 2; }

        /* HIGH-CONTRAST ENGINE LAYOUT */
        .engine-layout {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 40px;
            margin-bottom: 40px;
        }
        
        .panel {
            background: rgba(12, 12, 12, 0.8);
            border: 1px solid var(--border);
            border-top: 4px solid #222;
            border-radius: var(--radius);
            padding: 40px;
            transition: all 0.3s ease;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }
        .panel:hover {
            border-top-color: var(--accent);
            transform: translateY(-2px);
        }
        .full-width { grid-column: span 2; }
        
        /* DISTINCT HEADINGS */
        .panel h3 { 
            font-size: 14px; 
            text-transform: uppercase; 
            color: #fff; 
            margin-top: 0;
            margin-bottom: 30px; 
            letter-spacing: 2px; 
            border-bottom: 1px solid var(--border); 
            padding-bottom: 20px; 
        }
        
        .field-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(180px, 1fr));
            gap: 20px;
        }
        .field label { display: block; font-size: 10px; color: var(--text-dim); margin-bottom: 8px; font-weight: 700; text-transform: uppercase; }
        input {
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255,255,255,0.1);
            border-radius: 10px;
            color: white;
            padding: 14px;
            width: 100%;
            font-size: 14px;
            transition: 0.2s;
        }
        input:focus { outline: none; border-color: var(--accent); background: rgba(255,255,255,0.06); }

        .btn-predict {
            background: var(--text-main);
            color: black;
            border: none;
            padding: 24px;
            width: 100%;
            border-radius: 16px;
            font-weight: 800;
            font-size: 18px;
            cursor: pointer;
            transition: 0.3s;
            margin-bottom: 100px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .btn-predict:hover { background: var(--accent); color: white; transform: scale(1.01); }

        /* REVIEWS WITH IMAGES */
        .review-section {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 25px;
            margin-bottom: 100px;
        }
        .review-card {
            background: var(--glass);
            border: 1px solid var(--border);
            padding: 30px;
            border-radius: var(--radius);
        }
        .user-meta { display: flex; align-items: center; gap: 15px; margin-bottom: 20px; }
        .user-meta img { width: 50px; height: 50px; border-radius: 50%; border: 2px solid var(--accent); object-fit: cover; }
        .user-meta strong { font-size: 16px; color: #fff; display: block; }
        .user-meta span { font-size: 12px; color: var(--text-dim); }
        .review-card p { font-size: 14px; color: var(--text-dim); line-height: 1.6; font-style: italic; }

        /* EXPANDED FOOTER */
        footer {
            background: #000;
            padding: 80px 50px;
            border-top: 1px solid var(--border);
        }
        .footer-grid {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: 2fr 1fr 1fr 1fr;
            gap: 60px;
        }
        .footer-col h5 { color: #fff; margin-bottom: 25px; font-size: 12px; letter-spacing: 1px; text-transform: uppercase; }
        .footer-col a { display: block; color: var(--text-dim); text-decoration: none; margin-bottom: 15px; font-size: 14px; transition: 0.2s; }
        .footer-col a:hover { color: var(--accent); }

        #resultCard { display: none; }

        /* MOBILE RESPONSIVENESS */
        @media (max-width: 900px) {
            .bento-grid { grid-template-columns: 1fr; grid-auto-rows: auto; }
            .bento-card { grid-column: span 1 !important; grid-row: span 1 !important; }
            .engine-layout { grid-template-columns: 1fr; }
            .full-width { grid-column: span 1; }
            .review-section { grid-template-columns: 1fr; }
            .footer-grid { grid-template-columns: 1fr; gap: 40px; }
        }
      /* ---------- SLIDERS ---------- */

.slider-field{
display:flex;
flex-direction:column;
gap:8px;
}
label{
    font-size:10px;
    font-weight:700;
    text-transform:uppercase;
    color:var(--text-dim);
}

.slider-value{
font-size:12px;
color:var(--accent);
font-weight:700;
}

input[type=range]{
-webkit-appearance:none;
width:100%;
height:6px;
background:#222;
border-radius:10px;
outline:none;
}

input[type=range]::-webkit-slider-thumb{
-webkit-appearance:none;
appearance:none;
width:18px;
height:18px;
border-radius:50%;
background:var(--accent);
cursor:pointer;
box-shadow:0 0 8px rgba(255,60,60,0.8);
}

/* ---------- CHART AREA ---------- */

.chart-grid{
display:grid;
grid-template-columns:1fr 1fr;
gap:40px;
margin-top:40px;
}

.chart-box{
background:rgba(255,255,255,0.03);
padding:20px;
border-radius:14px;
border:1px solid var(--border);
}

.insights{
margin-top:30px;
background:rgba(255,60,60,0.05);
padding:20px;
border-radius:10px;
border-left:3px solid var(--accent);
font-size:14px;
color:var(--text-dim);
}  
    </style>
</head>
<body>

<nav class="navbar">
    <div class="nav-logo">PREDIX</div>
</nav>

<div class="container">
    <header>
        <h1>Intelligence for Longevity.</h1>
        <p>Predictive metabolic analysis using high-fidelity clinical datasets.</p>
    </header>

    <div class="bento-grid">
        <div class="bento-card span-8 row-2">
            <h4>Global Risk Distribution</h4>
            <div class="stat">783 Million</div>
            <p style="color: var(--text-dim); font-size: 14px;">Projected cases by 2045. Early detection via machine learning is the only scalable solution to the global metabolic crisis.</p>
            <div style="margin-top:20px; height: 100px; background: rgba(255,255,255,0.05); border-radius: 12px; display: flex; align-items: center; justify-content: center; color: #444; font-size: 12px; letter-spacing: 1px;">[ GLOBAL DISTRIBUTION HEATMAP ]</div>
        </div>
        <div class="bento-card span-4">
            <h4>Model Precision</h4>
            <div class="stat">94.2%</div>
        </div>
        <div class="bento-card span-4">
            <h4>Undiagnosed Cases</h4>
            <div class="stat">240M</div>
        </div>
        <div class="bento-card span-6">
            <h4>Annual Economic Burden</h4>
            <div class="stat">$1.3T</div>
        </div>
        <div class="bento-card span-6">
            <h4>Processing Speed</h4>
            <div class="stat">42ms</div>
        </div>
    </div>

    <div class="engine-layout">
        
        <div class="panel">
            <h3>Biometric Biomarkers</h3>
            <div class="field-grid">
                <div class="slider-field">

<label>BMI</label>

<input type="range" id="BMI" min="10" max="50" step="0.1" value="22"
oninput="bmiValue.innerText=this.value">

<div class="slider-value" id="bmiValue">22</div>

</div>


<div class="slider-field">

<label>Age</label>

<input type="range" id="Age" min="1" max="100" value="30"
oninput="ageValue.innerText=this.value">

<div class="slider-value" id="ageValue">30</div>

</div>

               <div class="slider-field">

<label>Gen. Health (1-5)</label>

<input type="range" min="1" max="5" step="1" value="3" id="GenHlth"
oninput="genValue.innerText=this.value">

<div class="slider-value" id="genValue">3</div>

</div>
                <div class="field"><label>Mental Health Days</label><input id="MentHlth" type="number"></div>
                <div class="field"><label>Phys. Health Days</label><input id="PhysHlth" type="number"></div>
                <div>
<label>Difficulty Walking</label>
<input type="range" min="0" max="1" step="1" value="0" id="DiffWalk"
oninput="cholVal.innerText=this.value==1?'YES':'NO'">
<div class="slider-value" id="cholVal">NO</div>
</div>

<label>BMI Category (1-5)</label>

<input type="range" min="1" max="5" step="1" value="3" id="BMI_Category"
oninput="genValue.innerText=this.value">

<div class="slider-value" id="genValue">3</div>

</div>
                <div class="slider-field">

<label>Age Group (1-5)</label>

<input type="range" min="1" max="5" step="1" value="3" id="Age_Group"
oninput="genValue.innerText=this.value">

<div class="slider-value" id="genValue">3</div>

</div>
                
                <div class="field"><label>Healthy Diet Score</label><input id="Healthy_Diet" type="number"></div>
            </div>
        </div>

     <div class="panel">

<h3>Cardiovascular Indicators</h3>

<div class="field-grid">

<div>
<label>High Blood Pressure</label>
<input type="range" min="0" max="1" step="1" value="0" id="HighBP"
oninput="bpVal.innerText=this.value==1?'YES':'NO'">
<div class="slider-value" id="bpVal">NO</div>
</div>

<div>
<label>High Cholesterol</label>
<input type="range" min="0" max="1" step="1" value="0" id="HighChol"
oninput="cholVal.innerText=this.value==1?'YES':'NO'">
<div class="slider-value" id="cholVal">NO</div>
</div>

<div>
<label>Cholesterol Check</label>
<input type="range" min="0" max="1" step="1" value="0" id="CholCheck"
oninput="cholcheckVal.innerText=this.value==1?'YES':'NO'">
<div class="slider-value" id="cholcheckVal">NO</div>
</div>

<div>
<label>Stroke History</label>
<input type="range" min="0" max="1" step="1" value="0" id="Stroke"
oninput="strokeVal.innerText=this.value==1?'YES':'NO'">
<div class="slider-value" id="strokeVal">NO</div>
</div>

<div>
<label>Heart Disease</label>
<input type="range" min="0" max="1" step="1" value="0" id="HeartDiseaseorAttack"
oninput="heartVal.innerText=this.value==1?'YES':'NO'">
<div class="slider-value" id="heartVal">NO</div>
</div>



</div>

</div>

    <div class="panel full-width" style="margin-bottom: 60px;">
        <h3>Social & Behavioral Determinants</h3>
        <div class="field-grid">
            
<div>
<label>Physical Activity</label>
<input type="range" min="0" max="1" step="1" value="0" id="PhysActivity"
oninput="actVal.innerText=this.value==1?'ACTIVE':'LOW'">
<div class="slider-value" id="actVal">LOW</div>
</div>
            <div>
<label>Smoking Status</label>
<input type="range" min="0" max="1" step="1" value="0" id="Smoker"
oninput="smokeVal.innerText=this.value==1?'YES':'NO'">
<div class="slider-value" id="smokeVal">NO</div>
</div>
            <div>
<label>Heavy Alcohol Consumption</label>
<input type="range" min="0" max="1" step="1" value="0" id="HvyAlcoholConsump"
oninput="alcVal.innerText=this.value==1?'YES':'NO'">
<div class="slider-value" id="alcVal">NO</div>
</div>
<div>
<label>Fruit Intake</label>
<input type="range" min="0" max="1" step="1" value="1" id="Fruits"
oninput="fruitVal.innerText=this.value==1?'YES':'NO'">
<div class="slider-value" id="fruitVal">YES</div>
</div>
<div>
<label>Vegetable Intake</label>
<input type="range" min="0" max="1" step="1" value="1" id="Veggies"
oninput="vegVal.innerText=this.value==1?'YES':'NO'">
<div class="slider-value" id="vegVal">YES</div>
</div>
       <div>
<label>Healthcare Access</label>
<input type="range" min="0" max="1" step="1" value="1" id="AnyHealthcare">

<div class="slider-value" id="vegVal">YES</div>
</div>     
           
          <div>
<label>No Doc</label>
<input type="range" min="0" max="1" step="1" value="1" id="NoDocbcCost">

<div class="slider-value" id="vegVal">YES</div>
</div>    

            <div class="slider-field">
<label>Biological Sex</label>
<input type="range" min="0" max="1" step="1" value="0" id="Sex">
<div class="slider-values">
<span>0 = Female</span>
<span>1 = Male</span>
</div>
</div>
            <div class="slider-field">
<label>Education Level</label>
<input type="range" min="0" max="5" step="1" value="0" id="Education">
<div class="slider-values">
<span>0 = No School</span>
<span>5 = College Grad</span>
</div>
</div>
      <div class="slider-field">
<label>Income Tier</label>
<input type="range" min="0" max="2" step="1" value="1" id="Income">
<div class="slider-values">
<span>0 = Low</span>
<span>2 = High</span>
</div>
</div>     
        </div>
    </div>

    <button class="btn-predict" id="analyzeBtn" onclick="runInference()">Analyse Risk</button>

    <div id="resultCard" class="panel full-width" style="margin-bottom: 80px; border: 1px solid var(--accent);">
        <h2 style="text-align: center; color: var(--accent); letter-spacing: 2px; margin-top: 0;">ANALYSIS COMPLETE</h2>
        <div style="text-align: center; font-size: 82px; font-weight: 800; margin: 20px 0;" id="riskValue">0%</div>
        <div id="riskLabel" style="text-align: center; font-weight: 700; font-size: 20px;"></div>
        <div id="aiExplanation" style="background: rgba(255,60,60,0.05); padding: 25px; border-radius: 12px; margin-top: 30px; border-left: 3px solid var(--accent); font-size: 14px; color: var(--text-dim); line-height: 1.6;"></div>
    </div>
    <div id="chartsArea" class="panel full-width" style="display:none">

<h3>Clinical Visualization</h3>

<div class="chart-grid">

<div class="chart-box">
<canvas id="riskChart"></canvas>
</div>

<div class="chart-box">
<canvas id="radarChart"></canvas>
</div>

<div class="chart-box" style="grid-column:span 2">
<canvas id="lifestyleChart"></canvas>
</div>

</div>

<div id="insightText" class="insights"></div>

</div>

    <div class="review-section">
        <div class="review-card">
            <div class="user-meta">
                <img src="https://i.pravatar.cc/150?u=dr1" alt="Reviewer">
                <div><strong>Dr. Aris Morgan</strong><span>Endocrinologist</span></div>
            </div>
            <p>"Predix has redefined how we approach early diabetic screening. The model's cross-referencing of 28 markers is exceptional."</p>
        </div>
        <div class="review-card">
            <div class="user-meta">
                <img src="https://i.pravatar.cc/150?u=tech2" alt="Reviewer">
                <div><strong>Marcus Chen</strong><span>HealthTech Architect</span></div>
            </div>
            <p>"A masterclass in minimal UI for complex clinical data. The speed of the inference engine is a benchmark for the industry."</p>
        </div>
        <div class="review-card">
            <div class="user-meta">
                <img src="https://i.pravatar.cc/150?u=res3" alt="Reviewer">
                <div><strong>Sarah Jenkins</strong><span>Medical Researcher</span></div>
            </div>
            <p>"Essential tool for identifying risk vectors in undiagnosed populations. The logic behind the social determinants panel is solid."</p>
        </div>
    </div>
</div>

<footer>
    <div class="footer-grid">
        <div class="footer-col">
            <h2 style="color: var(--accent); margin: 0; font-weight: 800; letter-spacing: -1px;">PREDIX</h2>
            <p style="margin-top: 15px; font-size: 14px; color: var(--text-dim); line-height: 1.6;">Advancing metabolic intelligence through decentralized neural computing and clinical analytics.</p>
        </div>
        <div class="footer-col">
            <h5>Intelligence</h5>
            <a href="#">Analysis Engine</a>
            <a href="#">Dataset Specs</a>
            <a href="#">Inference API</a>
        </div>
        <div class="footer-col">
            <h5>Research</h5>
            <a href="#">Global Trends</a>
            <a href="#">Privacy Protocol</a>
            <a href="#">Model Validation</a>
        </div>
        <div class="footer-col">
            <h5>Project</h5>
            <a href="#">Documentation</a>
            <a href="#">Contact Team</a>
            <a href="#">Source Code</a>
        </div>
    </div>
</footer>

<script>
    async function runInference() {

        const btn = document.getElementById("analyzeBtn");
        const originalText = btn.innerText;
        btn.innerText = "Processing Data...";
        
        const data = {};
document.querySelectorAll("input").forEach(i => data[i.id] = Number(i.value) || 0);

// add backend-required derived fields
data.Chol_Check_Interaction = data.HighChol * data.CholCheck;
data.HealthBurden = data.MentHlth + data.PhysHlth;
data.LifestyleRisk = data.Smoker + data.HvyAlcoholConsump;
data.Alcohol = data.HvyAlcoholConsump;
        
        try {
            // Use local backend when running locally; fallback to hosted backend.
            const API_BASE =
                (window.PREDIX_API_BASE && String(window.PREDIX_API_BASE)) ||
                (location.hostname === "localhost" || location.hostname === "127.0.0.1"
                    ? "http://127.0.0.1:8000"
                    : "https://predix-backend-l3dq.onrender.com");

            const response = await fetch(`${API_BASE}/api/v1/predict`, {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify(data)
            });
            const result = await response.json();
            console.log(result)
            
            document.getElementById("resultCard").style.display = "block";
            const risk = result.risk_score;
            generateCharts(data,risk)
            document.getElementById("riskValue").innerText = risk + "%";
            document.getElementById("riskValue").style.color = risk > 70 ? "#ff3c3c" : (risk > 40 ? "#f59e0b" : "#22c55e");
            document.getElementById("riskLabel").innerText = risk > 70 ? "CRITICAL RISK PROFILE" : (risk > 40 ? "MODERATE CONCERN" : "STABLE STATUS");
           document.getElementById("aiExplanation").innerText =
`AI Summary: Based on 28 aggregated clinical indicators, the neural network identifies a ${risk}% risk probability. High priority markers evaluated across Biometric, Cardiovascular, and Behavioral data points.`;
            
            // Scroll to results
            document.getElementById("resultCard").scrollIntoView({ behavior: 'smooth', block: 'center' });
            
        } catch (e) { 
            console.error(e); 
            alert("Error connecting to the intelligence engine. Please try again.");
        } finally {
            btn.innerText = originalText;
        }
    }
    function generateCharts(data,risk){

document.getElementById("chartsArea").style.display="block"

new Chart(document.getElementById("riskChart"),{

type:"doughnut",

data:{
labels:["Safe","Risk"],
datasets:[{
data:[100-risk,risk]
}]
}

})


new Chart(document.getElementById("radarChart"),{

type:"radar",

data:{
labels:["BMI","Blood Pressure","Cholesterol","Activity","Diet","Smoking"],

datasets:[{
label:"Health Indicators",

data:[
data.BMI,
data.HighBP,
data.HighChol,
data.PhysActivity,
data.Healthy_Diet,
data.Smoker
]

}]
}

})


new Chart(document.getElementById("lifestyleChart"),{

type:"bar",

data:{
labels:["Exercise","Diet","Smoking","Alcohol","Healthcare"],

datasets:[{
label:"Lifestyle Risk",

data:[
data.PhysActivity,
data.Healthy_Diet,
data.Smoker,
data.HvyAlcoholConsump,
data.AnyHealthcare
]

}]
}

})

generateInsights(data,risk)

}


function generateInsights(data,risk){

let tips=[]

if(data.BMI>30)
tips.push("High BMI detected. Weight reduction recommended.")

if(data.HighBP==1)
tips.push("Blood pressure risk marker present.")

if(data.HighChol==1)
tips.push("Cholesterol levels likely elevated.")

if(data.Smoker==1)
tips.push("Smoking significantly increases cardiovascular risk.")

if(data.PhysActivity==0)
tips.push("Low physical activity detected.")

if(risk>70)
tips.push("High diabetes risk. Clinical screening advised.")

document.getElementById("insightText").innerHTML=
"<b>AI Health Insights</b><br><br>"+tips.join("<br>")

}
    
</script>

</body>
</html>
