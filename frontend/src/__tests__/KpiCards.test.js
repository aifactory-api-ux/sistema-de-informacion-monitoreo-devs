import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom/extend-expect';
import KpiCards from '../components/KpiCards/KpiCards';

const mockKpis = [
  { title: 'Commits', value: 120, trend: 'up' },
  { title: 'Code Reviews', value: 45, trend: 'down' },
  { title: 'Deployments', value: 30, trend: 'up' },
  { title: 'Bug Fixes', value: 15, trend: 'stable' },
  { title: 'PR Reviews', value: 60, trend: 'up' }
];

describe('KpiCards Component', () => {
  test('renders KPI cards', () => {
    render(<KpiCards kpis={mockKpis} />);
    mockKpis.forEach(kpi => {
      expect(screen.getByText(kpi.title)).toBeInTheDocument();
      expect(screen.getByText(kpi.value.toString())).toBeInTheDocument();
      expect(screen.getByText(kpi.trend)).toBeInTheDocument();
    });
  });
});
