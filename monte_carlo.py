import numpy as np
import matplotlib.pyplot as plt
import pymc3 as pm

RADIUS= 1.7
def in_quarter_circle(x,y,radius):
    assert x > 0 and y > 0, "only looks at quarter circle"
    if x**2 + y**2 <=radius:
        return 1
    else:
        return 0

def generate_points(radius, n_points):
    x_points =np.random.random(n_points)
    y_points =np.random.random(n_points)
    return x_points, y_points
def find_pi(n_points = 100_000):
    radius = 1
    xp, yp = generate_points(radius,n_points)
    in_circle = 0
    for i in range(n_points):
        in_circle += in_quarter_circle(xp[i], yp[i], radius)
    return in_circle*4/n_points

def graph_accuracy_monte_carlo(n_points = 10_000):
    radius = 1
    mod_num = 10
    xp, yp = generate_points(radius,n_points)
    in_circle = 0
    calculations_of_pi = np.zeros(n_points//mod_num)
    for i in range(n_points):
        in_circle += in_quarter_circle(xp[i], yp[i], radius)
        if (i+1)%mod_num==0:
            calculations_of_pi[(i+1)//mod_num-1]= in_circle*4/(i+1)
    plt.plot(calculations_of_pi)
    plt.ylabel("Estimate of PI")
    plt.xlabel("number of data points in "+str(mod_num) + "s")
    plt.title("Graphing Monte Carlo Estimation of Pi over time")
    plt.savefig('graph_accuracy_monte_carlo.png')
    return in_circle*4/n_points

def find_radius(radius, n_points):
    print("this doesn't work")
    return
    upper = 5
    assert radius**2 < upper
    x_values, y_values = generate_points(radius,n_points)
    sleep_obs = np.zeros(n_points)
    for i in range(n_points):
        sleep_obs = in_quarter_circle(x_values[i], y_values[i], radius)
    with pm.Model() as sleep_model:
        # Create the alpha and beta parameters
        radius_2 = pm.Uniform('alpha', lower=0, upper=upper)
        
        # Create the probability from sqrt i.e. function representing quarter circle
        p = pm.Deterministic('p',np.sqrt(radius_2 - x_values**2) )
        
        # Create the bernoulli parameter which uses the observed data
        observed = pm.Bernoulli('obs', p, observed=sleep_obs)
        
        # Starting values are found through Maximum A Posterior estimation
        # start = pm.find_MAP()
        
        # Using Metropolis Hastings Sampling
        step = pm.Metropolis()
        
        # Sample from the posterior using the sampling method
        sleep_trace = pm.sample(n_points, step=step);    
    plt.plot(np.sqrt(sleep_trace['radius_2']))
    plt.savefig("MCMC_radius_over_time.png")

if __name__=='__main__':
    n_points = 100_000
    print("Monte Carlo sampling to find pi")
    print("value of pi is:", round(find_pi(n_points),2))
    print()
    graph_accuracy_monte_carlo(n_points)