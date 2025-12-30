import React, { useState } from 'react';
import { 
  Heart, Activity, AlertTriangle, CheckCircle, ChevronRight, ChevronLeft, 
  RefreshCw, User, Cigarette, BookOpen, ListChecks, Info, Terminal, 
  ShieldAlert, ClipboardList, Stethoscope, HeartPulse, Timer, Zap
} from 'lucide-react';
import './App.css';

/**
 * ==========================================
 * MODULE 2: API SERVICE
 * ==========================================
 */
const apiService = {
  diagnose: async (formData) => {
    try {
      const response = await fetch('http://127.0.0.1:8000/api/diagnose', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData)
      });
      if (!response.ok) throw new Error("Server returned an error");
      return await response.json();
    } catch {
      throw new Error("Connection Failed: Ensure your FastAPI server (main.py) is running on port 8000.");
    }
  }
};

/**
 * ==========================================
 * MODULE 3: MAIN APPLICATION (App.jsx)
 * ==========================================
 */
const App = () => {
  const [step, setStep] = useState(1);
  const [formData, setFormData] = useState({
    age_group: "Young Adult",
    gender: "Female",
    chest_pain: "None",
    short_breath: "No",
    fatigue: "No",
    dizziness: "No",
    cold_sweat: "No",
    smoker: "Non-Smoker",
    diabetes: "No",
    blood_pressure: "Normal",
    family_history: "No",
    inactive: "Active"
  });
  
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const updateField = (field, value) => {
    setFormData(prev => ({ ...prev, [field]: value }));
  };

  const handleNext = () => setStep(2);
  const handleBack = () => setStep(1);

  const handleSubmit = async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await apiService.diagnose(formData);
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const resetForm = () => {
    setStep(1);
    setResult(null);
    setError(null);
  };

  const renderStep = () => {
    if (step === 1) {
      return (
        <div className="animate-step form-section">
          <div className="section-title">
            <h2>Phase 1: Symptoms</h2>
            <p>Demographic and Physical Indicators</p>
          </div>

          <div className="grid-2">
            <div className="field-group">
              <div className="field-label"><User size={12}/> Age Group</div>
              <select value={formData.age_group} onChange={(e) => updateField('age_group', e.target.value)}>
                <option>Young Adult</option><option>Middle-Aged Adult</option><option>Elderly</option>
              </select>
            </div>
            <div className="field-group">
              <div className="field-label"><User size={12}/> Gender</div>
              <select value={formData.gender} onChange={(e) => updateField('gender', e.target.value)}>
                <option>Male</option><option>Female</option>
              </select>
            </div>
          </div>

          <div className="field-group">
            <div className="field-label"><HeartPulse size={12}/> Chest Pain Severity</div>
            <div className="option-grid">
              {['None', 'Mild', 'Moderate', 'Severe'].map(level => (
                <button 
                  key={level} 
                  className={`card-option ${formData.chest_pain === level ? 'active' : ''}`}
                  onClick={() => updateField('chest_pain', level)}
                >
                  {level}
                </button>
              ))}
            </div>
          </div>

          <div className="grid-2">
             {['short_breath', 'fatigue', 'dizziness', 'cold_sweat'].map((f) => (
               <div key={f} className="field-group">
                 <div className="field-label"><Activity size={12}/> {f.replace('_', ' ')}?</div>
                 <select value={formData[f]} onChange={(e) => updateField(f, e.target.value)}>
                   <option>No</option><option>Yes</option>
                 </select>
               </div>
             ))}
          </div>

          <button className="btn btn-primary" onClick={handleNext}>
            Continue Phase 2 <ChevronRight size={18} />
          </button>
        </div>
      );
    }

    return (
      <div className="animate-step form-section">
        <div className="section-title">
          <h2>Phase 2: History</h2>
          <p>Medical Background & Lifestyle Habits</p>
        </div>

        <div className="grid-2">
            <div className="field-group">
              <div className="field-label"><Cigarette size={12}/> Smoking</div>
              <select value={formData.smoker} onChange={(e) => updateField('smoker', e.target.value)}>
                <option>Non-Smoker</option><option>Smoker</option>
              </select>
            </div>
            <div className="field-group">
              <div className="field-label"><ClipboardList size={12}/> Diabetes</div>
              <select value={formData.diabetes} onChange={(e) => updateField('diabetes', e.target.value)}>
                <option>No</option><option>Yes</option>
              </select>
            </div>
            <div className="field-group">
              <div className="field-label"><Activity size={12}/> Blood Pressure</div>
              <select value={formData.blood_pressure} onChange={(e) => updateField('blood_pressure', e.target.value)}>
                <option>Normal</option><option>Elevated</option><option>High</option>
              </select>
            </div>
            <div className="field-group">
              <div className="field-label"><ShieldAlert size={12}/> Family History</div>
              <select value={formData.family_history} onChange={(e) => updateField('family_history', e.target.value)}>
                <option>No</option><option>Yes</option>
              </select>
            </div>
        </div>

        <div className="field-group">
          <div className="field-label"><Activity size={12}/> Physical Activity</div>
          <select value={formData.inactive} onChange={(e) => updateField('inactive', e.target.value)}>
            <option>Active</option><option>Physically Inactive</option>
          </select>
        </div>

        <div className="grid-2">
          <button className="btn btn-back" onClick={handleBack}>Back</button>
          <button className="btn btn-action" onClick={handleSubmit} disabled={loading}>
            {loading ? <RefreshCw className="animate-spin" size={18}/> : <ShieldAlert size={18}/>}
            {loading ? "Analyzing..." : "Analyze Profile"}
          </button>
        </div>
      </div>
    );
  };

  return (
    <div className="app-wrapper">
      
      <div className="main-container">
        
        {/* Header Section */}
        <div className="header">
          <div className="header-top">
            <div className="brand">
              <div className="brand-icon">
                <Heart size={24} fill="currentColor" />
              </div>
              <div className="brand-text">
                <h1>Heart Attack Pre Screening <span>Expert System </span></h1>
                <p></p>
              </div>
            </div>
            {!result && <div className="phase-badge">PHASE {step} / 2</div>}
          </div>
          
          {!result && (
            <div className="progress-bar-container">
              <div className="progress-fill" style={{ width: `${(step / 2) * 100}%` }} />
            </div>
          )}
        </div>

        <div className="content-padding">
          {error && (
            <div style={{ background: '#fff1f2', color: '#e11d48', padding: '1rem', borderRadius: '1rem', marginBottom: '2rem', fontSize: '0.8rem', fontWeight: 'bold', display: 'flex', gap: '0.5rem' }}>
              <Terminal size={16}/> {error}
            </div>
          )}

          {!result ? renderStep() : (
            <div className="animate-step result-view">
              <div className="result-header">
                <div className={`diagnosis-circle ${result.diagnosis === 'High Risk' ? 'high' : result.diagnosis === 'Moderate Risk' ? 'mod' : 'low'}`}>
                  {result.diagnosis === 'High Risk' ? <AlertTriangle size={48} /> : 
                   result.diagnosis === 'Moderate Risk' ? <Activity size={48} /> : 
                   <CheckCircle size={48} />}
                </div>
                <div>
                  <div className="risk-badge" style={{ background: result.diagnosis === 'High Risk' ? '#dc2626' : result.diagnosis === 'Moderate Risk' ? '#f59e0b' : '#10b981' }}>
                    {result.diagnosis} Level
                  </div>
                  <h2 style={{ fontSize: '2rem', fontWeight: '900', marginTop: '1rem' }}>{result.title}</h2>
                  <p style={{ color: '#64748b', fontWeight: 'bold', marginTop: '0.5rem' }}>{result.summary_message}</p>
                </div>
              </div>

              <div className="rule-box">
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.5rem' }}>
                  <Info size={14} color="#3b82f6" />
                  <span style={{ fontSize: '9px', fontWeight: '900', color: '#64748b', textTransform: 'uppercase' }}>Expert Logic Trace</span>
                </div>
                <p>{result.triggered_rule.id}: {result.triggered_rule.full_logic}</p>
              </div>

              <div className="results-grid">
                <div className="info-card">
                  <h3 style={{ color: '#1d4ed8' }}><ListChecks size={18}/> Recommendations</h3>
                  <ul className="info-list">
                    {result.recommendations.map((rec, i) => (
                      <li key={i} className="info-item">
                        <span className="item-num">{i+1}</span> {rec}
                      </li>
                    ))}
                  </ul>
                </div>
                <div className="info-card">
                  <h3 style={{ color: '#047857' }}><BookOpen size={18}/> Education</h3>
                  <ul className="info-list">
                    {result.educational_tips.map((tip, i) => (
                      <li key={i} className="info-item">
                        <CheckCircle size={14} color="#10b981" style={{ flexShrink: 0, marginTop: '2px' }} /> {tip}
                      </li>
                    ))}
                  </ul>
                </div>
              </div>

              <button className="btn btn-primary" onClick={resetForm}>
                <RefreshCw size={18} /> Restart Engine
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default App;