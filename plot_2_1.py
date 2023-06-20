import numpy as np
import plotly.graph_objects as go
from scipy.stats import norm
import schemes
import matplotlib.pyplot as plt

N = 5000
M = 1000
T = 10

u=-2
D=1
values, means, sigma, p_val = schemes.distributions(u,D,M,T,N)


x = np.arange(np.amin(values),np.amax(values),0.01)
fig = go.Figure()

for step in range(100):
    fig.add_trace(
        go.Scatter(
            visible=False,
            name = f'step: {str(step)}',
            x=x,
            y=norm.pdf(x,means[int(step*N/100)],sigma[int(step*N/100)])
        )
    )
fig.data[0].visible = True

steps = []
for i in range(100):
    step = dict(
        method="update",
        args=[{"visible": [False]* 100},
              {"title": "Slider switched to step: " + str(i)}],
    )
    step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
    steps.append(step)

sliders = [dict(
    active=0,
    currentvalue={"prefix": "snapshot: "},
    pad={"t": 100},
    steps=steps
)]

fig.update_layout(
    sliders=sliders
)

fig.write_html('plots/interactive_21.html')

fig_mu, ax_mu = plt.subplots()

ax_mu.plot(np.arange(N),means,color='red',label='numerically calculated mean')
ax_mu.plot(np.arange(N),-u*T/N*np.arange(N),color='blue',label='methematically calculated mean')
ax_mu.set_title('Mean for u=-2 and D=1')
ax_mu.set_ylabel('Mean')
ax_mu.set_xlabel('step')
fig_mu.legend()
fig_mu.set_size_inches(11.69,8.27)

fig_mu.savefig('plots/mean_21.png')
fig_sigma, ax_sigma = plt.subplots()

ax_sigma.plot(np.arange(N),sigma,color='red',label='numerically calculated SD')
ax_sigma.plot(np.arange(N),np.sqrt(2*D*T/N*np.arange(N)),color='blue',label='methematically calculated SD')
fig_sigma.legend()
ax_sigma.set_title('SD for u=-2 and D=1')
ax_sigma.set_ylabel('SD')
ax_sigma.set_xlabel('step')
fig_sigma.set_size_inches(11.69,8.27)

fig_sigma.savefig('plots/SD_21.png')