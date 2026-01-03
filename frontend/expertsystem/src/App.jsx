import React, { useState } from 'react';
import { 
  Heart, 
  Activity, 
  Stethoscope, 
  AlertCircle, 
  CheckCircle2, 
  ChevronRight, 
  Info, 
  User, 
  Zap,
  ArrowRight,
  RefreshCw,
  ClipboardList,
  ShieldCheck,
  Thermometer
} from 'lucide-react';
import './App.css';

const App = () => {
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);
  
  const [formData, setFormData] = useState({
    age_group: 'Young Adult',
    gender: 'Male',
    chest_pain: 'None',
    short_breath: 'No',
    fatigue: 'No',
    dizziness: 'No',
    cold_sweat: 'No',
    smoker: 'Non-Smoker',
    diabetes: 'No',
    blood_pressure: 'Normal',
    family_history: 'No',
    inactive: 'Active'
  });

  const handleChange = (name, value) => {
    setFormData(prev => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await fetch('http://127.0.0.1:8000/api/diagnose', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error('Medical server unreachable. Ensure FastAPI is active on port 8000.');
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const ToggleGroup = ({ label, name, value, options }) => (
    <div className="input-group">
      <label className="label">{label}</label>
      <div className="toggle-container">
        {options.map((opt) => (
          <button
            key={opt.value}
            type="button"
            className={`toggle-btn ${value === opt.value ? 'active' : ''}`}
            onClick={() => handleChange(name, opt.value)}
          >
            {opt.label}
          </button>
        ))}
      </div>
    </div>
  );

  return (
    <div className="app-container">
    

      <nav>
        <div className="nav-inner">
          <div className="logo">
            <div className="logo-box"><Heart size={18} fill="currentColor" /></div>
            <span>HEART<span style={{color: 'var(--primary-red)'}}>EXPERT</span></span>
          </div>
        </div>
      </nav>

<main>
        {!result ? (
          <>
            <div className="hero">
              <h1> <span style={{color: 'var(--primary-red)'}}>Heart Attack</span> Pre Screening.</h1>
              <p>Rule-Based Expert System for Early Heart Attack Risk Pre-Assessment.</p>
            </div>

            <div className="grid-layout">
              <form onSubmit={handleSubmit}>
                {/* 1. DEMOGRAPHICS (GP STYLE) */}
                <div className="card">
                  <div className="card-header">
                    <div className="icon-circle"style={{background: 'var(--primary-red)'}}><User size={20} /></div>
                    <h2 className="card-title">Patient Profile</h2>
                  </div>
                  <div className="gp-row">
                    <div className="input-group">
                      <label className="label">Age Group</label>
                      <select value={formData.age_group} onChange={(e) => handleChange('age_group', e.target.value)}>
                        <option value="Young Adult">Young Adult (&lt;40)</option>
                        <option value="Middle-Aged Adult">Middle-Aged (40-59)</option>
                        <option value="Elderly">Elderly (≥60)</option>
                      </select>
                    </div>
                    <div className="input-group">
                      <label className="label">Gender</label>
                      <select value={formData.gender} onChange={(e) => handleChange('gender', e.target.value)}>
                        <option value="Male">Male</option>
                        <option value="Female">Female</option>
                      </select>
                    </div>
                  </div>
                  
                  <div className="input-group" style={{marginTop: '20px'}}>
                    <label className="label">Chest Pain Assessment</label>
                    <select value={formData.chest_pain} onChange={(e) => handleChange('chest_pain', e.target.value)}>
                      <option value="None">No Chest Pain</option>
                      <option value="Mild">Mild / Discomfort</option>
                      <option value="Moderate">Moderate / Constricting</option>
                      <option value="Severe">Severe / Intense Pain</option>
                    </select>
                  </div>
                </div>

                {/* 2. SYMPTOMS (YES/NO TOGGLES) */}
                <div className="card">
                  <div className="card-header">
                    <div className="icon-circle" style={{background: 'var(--primary-red)'}}><Thermometer size={20} /></div>
                    <h2 className="card-title">Symptom Checklist</h2>
                  </div>
                  <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '24px'}}>
                    <ToggleGroup 
                      label="Shortness of Breath" 
                      name="short_breath" 
                      value={formData.short_breath} 
                      options={[{label: 'No', value: 'No'}, {label: 'Yes', value: 'Yes'}]} 
                    />
                    <ToggleGroup 
                      label="Cold Sweating" 
                      name="cold_sweat" 
                      value={formData.cold_sweat} 
                      options={[{label: 'No', value: 'No'}, {label: 'Yes', value: 'Yes'}]} 
                    />
                    <ToggleGroup 
                      label="Dizziness / Nausea" 
                      name="dizziness" 
                      value={formData.dizziness} 
                      options={[{label: 'No', value: 'No'}, {label: 'Yes', value: 'Yes'}]} 
                    />
                    <ToggleGroup 
                      label="Chronic Fatigue" 
                      name="fatigue" 
                      value={formData.fatigue} 
                      options={[{label: 'No', value: 'No'}, {label: 'Yes', value: 'Yes'}]} 
                    />
                  </div>
                </div>

                {/* 3. CLINICAL & LIFESTYLE */}
                <div className="card">
                  <div className="card-header">
                    <div className="icon-circle" style={{background: 'var(--primary-red)'}}><Activity size={20} /></div>
                    <h2 className="card-title">Clinical History</h2>
                  </div>
                  <div className="input-group" style={{marginBottom: '24px'}}>
                    <label className="label">Blood Pressure Level</label>
                    <select value={formData.blood_pressure} onChange={(e) => handleChange('blood_pressure', e.target.value)}>
                      <option value="Normal">Normal (&lt;120)</option>
                      <option value="Elevated">Elevated (120-139)</option>
                      <option value="High">High (≥140)</option>
                    </select>
                  </div>
                  
                  <div style={{display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '24px'}}>
                    <ToggleGroup 
                      label="Diabetes" 
                      name="diabetes" 
                      value={formData.diabetes} 
                      options={[{label: 'No', value: 'No'}, {label: 'Yes', value: 'Yes'}]} 
                    />
                    <ToggleGroup 
                      label="Family History" 
                      name="family_history" 
                      value={formData.family_history} 
                      options={[{label: 'No', value: 'No'}, {label: 'Yes', value: 'Yes'}]} 
                    />
                    <ToggleGroup 
                      label="Smoking Status" 
                      name="smoker" 
                      value={formData.smoker} 
                      options={[{label: 'No', value: 'Non-Smoker'}, {label: 'Yes', value: 'Smoker'}]} 
                    />
                    <ToggleGroup 
                      label="Activity Level" 
                      name="inactive" 
                      value={formData.inactive} 
                      options={[{label: 'Active', value: 'Active'}, {label: 'Inactive', value: 'Physically Inactive'}]} 
                    />
                  </div>
                </div>

                <button type="submit" className="btn-submit" disabled={loading}>
                  {loading ? <RefreshCw className="spin" size={24} /> : <>RUN EXPERT ANALYSIS <ArrowRight size={20}/></>}
                </button>

                {error && <div className="error-toast"><AlertCircle size={18}/> {error}</div>}
              </form>


              <aside>
                <div className="sidebar-card">
                  <div style={{display: 'flex', alignItems: 'center', gap: '10px', marginBottom: '24px'}}>
                    <ClipboardList size={20} color="var(--primary-red)" />
                    <h3 style={{fontSize: '1rem', fontWeight: 800}}>LIVE INDICATORS</h3>
                  </div>
                  <div style={{display: 'flex', flexDirection: 'column'}}>
                    {Object.entries(formData).map(([key, val]) => (
                      <div className="summary-item" key={key}>
                        <span className="summary-label">{key.replace('_', ' ')}</span>
                        <span className={`summary-value ${(val === 'Yes' || val === 'High' || val === 'Smoker' || val === 'Physically Inactive') ? 'risk' : ''}`}>{val}</span>
                      </div>
                    ))}
                  </div>
                </div>
              </aside>
            </div>
          </>
) : (
          <div style={{maxWidth: '800px', margin: '0 auto'}}>
            <div className={`report-card ${result.diagnosis === 'High Risk' ? 'risk-high' : result.diagnosis === 'Moderate Risk' ? 'risk-mod' : 'risk-low'}`}>
              <span style={{fontSize: '0.75rem', fontWeight: 900, textTransform: 'uppercase', letterSpacing: '2px', background: 'var(--primary-red)', color: 'white', padding: '5px 15px', borderRadius: '20px'}}>
                {result.triggered_rule.id}
              </span>
              <h2 className="diag-text">{result.diagnosis}</h2>
              <p style={{fontSize: '1.25rem', fontWeight: 700, opacity: 0.8, marginBottom: '32px'}}>{result.summary_message}</p>
              
              <div style={{background: result.diagnosis === 'High Risk' ? 'rgba(255,255,255,0.05)' : '#fff5f5', padding: '30px', borderRadius: '32px', textAlign: 'left', border: result.diagnosis === 'High Risk' ? '1px solid #333' : 'none'}}>
                <h4 style={{fontSize: '0.8rem', fontWeight: 800, marginBottom: '16px', textTransform: 'uppercase', color: result.diagnosis === 'High Risk' ? 'white' : 'var(--primary-red)'}}>Clinical Recommendations</h4>
                {result.recommendations.map((rec, i) => (
                  <div key={i} style={{display: 'flex', alignItems: 'center', gap: '15px', marginBottom: '12px', fontWeight: 700}}>
                    <Zap size={16} color="var(--primary-red)" fill="var(--primary-red)" />
                    {rec}
                  </div>
                ))}
              </div>
            </div>

            <div className="card" style={{marginTop: '30px'}}>
              <h3 style={{fontWeight: 800, fontSize: '1rem', marginBottom: '16px'}}>System Log Trace</h3>
              <div style={{background: '#fcfcfc', padding: '24px', borderRadius: '20px', fontSize: '0.85rem', fontFamily: 'monospace', lineHeight: 1.7, border: '1.5px solid #f0f0f0', color: '#555'}}>
                <span style={{color: 'var(--primary-red)', fontWeight: 800}}>IF:</span> {result.triggered_rule.full_logic.split('THEN')[0].replace('Rule ' + result.triggered_rule.id + ': IF ', '')}<br/>
                <span style={{color: 'var(--primary-red)', fontWeight: 800}}>THEN:</span> {result.diagnosis}
              </div>
            </div>

            <button onClick={() => setResult(null)} style={{width: '100%', padding: '24px', background: 'white', border: '2.5px solid #000', borderRadius: '24px', cursor: 'pointer', fontWeight: 800, fontSize: '1rem', transition: 'all 0.2s'}}>
              NEW PATIENT SCREENING
            </button>
          </div>
        )}
      </main>
    </div>
  );
};

export default App;