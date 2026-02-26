import React, { Suspense } from 'react';
import './Charts.css';

const LineChart = React.lazy(() => import('./LineChart'));
const BarChart = React.lazy(() => import('./BarChart'));

const Charts = () => {
  return (
    <div className="charts">
      <Suspense fallback={<div>Loading...</div>}>
        <LineChart />
        <BarChart />
      </Suspense>
    </div>
  );
};

export default Charts;
