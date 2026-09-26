import { useState } from "react";
import "./App.css";
function App() {
  const [selectedImage, setSelectedImage] = useState(null);
  const [analysisResult, setAnalysisResult] = useState(null);
  return (
    <div className="app">
      <header className="navbar">
        <div className="logo">🌱 CropGuard AI</div>

        <nav>
          <a href="#home">Home</a>
          <a href="#detection">Disease Detection</a>
          <a href="#severity">Severity</a>
          <a href="#agronomist">AI Agronomist</a>
          <a href="#reports">Reports</a>
        </nav>
      </header>

      <main>
        <section id="home" className="hero">
          <div>
            <p className="tagline">AI-POWERED CROP HEALTH</p>

            <h1>
              Protect Your Crops
              <br />
              With <span>AI</span>
            </h1>

            <p className="hero-text">
              Detect crop diseases from leaf images, understand disease
              severity, and get personalized treatment recommendations.
            </p>

            <a href="#detection" className="primary-button">
              Start Disease Detection
            </a>
          </div>

          <div className="hero-card">
            <div className="leaf-icon">🌿</div>
            <h2>Smart Crop Health</h2>
            <p>
              Fast disease identification and actionable insights for farmers.
            </p>
          </div>
        </section>

        <section id="detection" className="detection-section">
          <p className="section-label">DISEASE DETECTION</p>

          <h2>Upload a Leaf Image</h2>

          <p>
            Upload a clear image of a crop leaf to analyze it for possible
            diseases.
          </p>

          <div className="upload-box">
            <div className="upload-icon">📷</div>

            <h3>Upload your leaf image</h3>

            <p>PNG, JPG or JPEG</p>

            <label className="upload-button">
              Choose Image
              <input
  type="file"
  accept="image/*"
  onChange={(e) => setSelectedImage(e.target.files[0])}
/>
            </label>
            {selectedImage && (
  <div className="image-preview">
    <h3>Selected Leaf Image</h3>
    <img
      src={URL.createObjectURL(selectedImage)}
      alt="Selected crop leaf"
    />
    <p>{selectedImage.name}</p>
    <button
  className="analyze-button"
  onClick={() => setAnalysisResult("Image ready for disease analysis")}
>
  Analyze Image
</button>
{analysisResult && (
  <div className="analysis-result">
    <h3>Analysis Result</h3>
    <p>{analysisResult}</p>
  </div>
)}
  </div>
)}
          </div>
        </section>

        <section id="severity" className="feature-section">
          <div className="feature-card">
            <div className="feature-icon">🔬</div>
            <h3>Disease Detection</h3>
            <p>
              Identify potential crop diseases using AI-powered image
              analysis.
            </p>
          </div>

          <div className="feature-card">
            <div className="feature-icon">📊</div>
            <h3>Severity Analysis</h3>
            <p>
              Estimate disease severity so farmers can prioritize timely
              treatment.
            </p>
          </div>

          <div id="agronomist" className="feature-card">
            <div className="feature-icon">🤖</div>
            <h3>AI Agronomist</h3>
            <p>
              Get treatment recommendations and answers about crop health,
              prevention, and best practices.
            </p>
          </div>
        </section>

        <section id="reports" className="reports-section">
          <p className="section-label">CROP HEALTH MONITORING</p>

          <h2>Monitor Crop Health</h2>

          <p>
            Regional disease heatmaps and crop health reports can help identify
            disease patterns and support early intervention.
          </p>
        </section>
      </main>

      <footer>
        <p>© 2026 CropGuard AI — AI-powered crop disease surveillance</p>
      </footer>
    </div>
  );
}

export default App;