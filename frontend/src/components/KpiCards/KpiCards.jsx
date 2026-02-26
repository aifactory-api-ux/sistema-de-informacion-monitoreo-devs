import React, { useEffect, useState } from 'react';
import { fetchKpis } from '../../services/api';

function KpiCards() {
  const [kpis, setKpis] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadKpis = async () => {
      try {
        const data = await fetchKpis();
        setKpis(data);
      } catch (err) {
        setError('Failed to load KPIs');
      } finally {
        setLoading(false);
      }
    };
    loadKpis();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>{error}</div>;

  return (
    <div>
      {kpis.map((kpi, index) => (
        <div key={index}>
          <h3>{kpi.name}</h3>
          <p>Value: {kpi.value}</p>
          <p>Trend: {kpi.trend}</p>
        </div>
      ))}
    </div>
  );
}

export default KpiCards;
