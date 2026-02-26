import React from 'react';
import PropTypes from 'prop-types';
import './KpiCards.css';

const KpiCards = ({ kpis }) => {
  return (
    <div className="kpi-cards">
      {kpis.map((kpi, index) => (
        <div key={index} className="kpi-card">
          <h3>{kpi.title}</h3>
          <p>{kpi.value}</p>
          <span>{kpi.trend}</span>
        </div>
      ))}
    </div>
  );
};

KpiCards.propTypes = {
  kpis: PropTypes.arrayOf(
    PropTypes.shape({
      title: PropTypes.string.isRequired,
      value: PropTypes.oneOfType([PropTypes.string, PropTypes.number]).isRequired,
      trend: PropTypes.string.isRequired,
    })
  ).isRequired,
};

export default KpiCards;
