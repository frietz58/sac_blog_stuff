from spinup.utils.test_policy import load_policy, run_policy
import gym
import argparse


if __name__ =="__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--env', type=str, required=True)
    parser.add_argument('--save_dir', type=str, required=True)
    parser.add_argument("-d", '--deterministic', action="store_true")
    parser.add_argument("-e", "--episodes", type=int, default=100)
    parser.add_argument("-dr", "--dont_render", action="store_false")
    args = parser.parse_args()

    if args.dont_render == False:
        render_it = False
    else:
        render_it = True

    print(args.save_dir)

    _, get_action = load_policy(args.save_dir, deterministic=args.deterministic)
    env = gym.make(args.env)
    run_policy(env, get_action, num_episodes=args.episodes, render=render_it)

