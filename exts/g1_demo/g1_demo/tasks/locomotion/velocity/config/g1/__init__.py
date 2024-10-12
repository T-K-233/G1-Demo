
import gymnasium as gym

from .env_cfg import G1EnvCfg
from .agents.rsl_rl_ppo_cfg import G1PPORunnerCfg

##
# Register Gym environments.
##


gym.register(
    id="Velocity-G1-v0",
    entry_point="omni.isaac.lab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": G1EnvCfg,
        "rsl_rl_cfg_entry_point": G1PPORunnerCfg,
    },
)
