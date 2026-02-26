import React, { useEffect, useState } from 'react';
import { fetchDevelopers, fetchSprints, fetchMetrics } from '../../services/api';

function DataTable() {
  const [developers, setDevelopers] = useState([]);
  const [sprints, setSprints] = useState([]);
  const [metrics, setMetrics] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const loadData = async () => {
      try {
        const [devs, sprs, mets] = await Promise.all([
          fetchDevelopers(),
          fetchSprints(),
          fetchMetrics()
        ]);
        setDevelopers(devs);
        setSprints(sprs);
        setMetrics(mets);
      } catch (err) {
        setError('Failed to load data');
      } finally {
        setLoading(false);
      }
    };
    loadData();
  }, []);

  if (loading) return <div>Loading...</div>;
  if (error) return <div>{error}</div>;

  return (
    <div>
      <h2>Developers</h2>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Email</th>
          </tr>
        </thead>
        <tbody>
          {developers.map((dev) => (
            <tr key={dev.id}>
              <td>{dev.name}</td>
              <td>{dev.email}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <h2>Sprints</h2>
      <table>
        <thead>
          <tr>
            <th>Name</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          {sprints.map((sprint) => (
            <tr key={sprint.id}>
              <td>{sprint.name}</td>
              <td>{sprint.status}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <h2>Metrics</h2>
      <table>
        <thead>
          <tr>
            <th>Developer</th>
            <th>Commits</th>
            <th>Code Reviews</th>
          </tr>
        </thead>
        <tbody>
          {metrics.map((metric) => (
            <tr key={metric.id}>
              <td>{metric.developerName}</td>
              <td>{metric.commits}</td>
              <td>{metric.codeReviews}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default DataTable;
