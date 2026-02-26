import React from 'react';
import KpiCards from '../KpiCards/KpiCards';
import Charts from '../Charts/Charts';
import DataTable from '../DataTable/DataTable';

function Dashboard() {
  return (
    <div>
      <h1>Dashboard</h1>
      <KpiCards />
      <Charts />
      <DataTable />
    </div>
  );
}

export default Dashboard;
