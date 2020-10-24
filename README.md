# sac_blog_stuff

Data and code used in Soft Actor-Critic blog post.

`final_data` contains all data shown in post, but I deleted the model parameters, because they were rather big, so to see the algorithms in action, you would have to retrain.

Install DRL (https://github.com/createamind/DRL) with python 3.6 venv, otherwise spinup might throw some cryptic tensorflow errors...

Then just use spinup to train your agents, for example with implementations provided by DRL: 

```bash
# python -m spinup.run [algo name] [experiment flags]
python -m spinup.run sac1 --env BipedalWalkerHardcore-v3 --exp_name sac1 --epochs 500
```

And see the agents like this (except this wouldn't work with the data in the repo, because the deleted model file...):
```bash
# python -m spinup.run test_policy path/to/output_directory
python -m spinup.run test_policy final_data/sac_auto/sac_auto_s0/

```

