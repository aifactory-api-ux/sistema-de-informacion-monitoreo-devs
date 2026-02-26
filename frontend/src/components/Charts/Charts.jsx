import React, { Suspense } from 'react';

const LineChart = React.lazy(() => import('./LineChart'));
const BarChart = React.lazy(() => import('./BarChart'));

function Charts() {
  return (
    <div>
      <h2>Charts</h2>
      <Suspense fallback={<div>Loading charts...</div>}>
        <LineChart />
        <BarChart />
      </Suspense>
    </div>
  );
}

export default Charts;
