import json
import math

# Task 1: Read and parse JSON file manually
with open('data.json', 'r') as f:
    data = json.load(f)

warehouses = data['warehouses']
agents = data['agents']
packages = data['packages']

# Euclidean distance
def get_distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# Task 2: Assign each package to nearest agent based on distance from agent to warehouse
assigned = {agent_id: [] for agent_id in agents}

for pkg in packages:
    w_loc = warehouses[pkg['warehouse']]
    nearest_agent = None
    min_dist = float('inf')
    for agent_id, agent_loc in agents.items():
        dist = get_distance(agent_loc, w_loc)
        if dist < min_dist:
            min_dist = dist
            nearest_agent = agent_id
    assigned[nearest_agent].append(pkg)

# Task 3: Simulate delivery and compute total distance
total_distance = {}
for agent_id in agents:
    current_loc = agents[agent_id]
    total_dist = 0
    for pkg in assigned[agent_id]:
        w_loc = warehouses[pkg['warehouse']]
        dest = pkg['destination']
        total_dist += get_distance(current_loc, w_loc)
        total_dist += get_distance(w_loc, dest)
        current_loc = dest
    total_distance[agent_id] = round(total_dist, 2)

# Task 4: Generate report
report = {}
best_agent = None
min_efficiency = float('inf')

for agent_id in agents:
    count = len(assigned[agent_id])
    dist = total_distance[agent_id]
    efficiency = round(dist / count, 2) if count > 0 else 0

    report[agent_id] = {
        "packages_delivered": count,
        "total_distance": dist,
        "efficiency": efficiency
    }

    if count > 0 and efficiency < min_efficiency:
        min_efficiency = efficiency
        best_agent = agent_id

report["best_agent"] = best_agent

# Task 5: Save report to report.json
with open('report.json', 'w') as f:
    json.dump(report, f, indent=2)

print("Simulation Completed")
print(report)