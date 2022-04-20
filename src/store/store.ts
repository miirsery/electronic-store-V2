import {
  ActionContext,
  ActionTree,
  createLogger,
  createStore,
  GetterTree,
  MutationTree,
} from 'vuex'

export type State = {
  counter: number
  profileImage: string
}

const state: State = {
  counter: 0,
  profileImage: null,
}

export enum MutationTypes {
  INC_COUNTER = 'SET_COUNTER',
  SET_PROFILE_IMAGE = 'SET_PROFILE_IMAGE',
}

export enum ActionTypes {
  INC_COUNTER = 'SET_COUNTER',
}

export type Mutations<S = State> = {
  [MutationTypes.INC_COUNTER](state: S, payload: number): void
  [MutationTypes.SET_PROFILE_IMAGE](state: S, payload: string): void
}

// define mutations
const mutations: MutationTree<State> & Mutations = {
  [MutationTypes.INC_COUNTER](state: State, payload: number) {
    state.counter += payload
  },
  [MutationTypes.SET_PROFILE_IMAGE](state: State, payload: string) {
    state.profileImage = payload
  },
}

// actions

type AugmentedActionContext = {
  commit<K extends keyof Mutations>(
    key: K,
    payload: Parameters<Mutations[K]>[1]
  ): ReturnType<Mutations[K]>
} & Omit<ActionContext<State, State>, 'commit'>

//actions interface

export interface Actions {
  [ActionTypes.INC_COUNTER](
    { commit }: AugmentedActionContext,
    payload: number
  ): void
}

export const actions: ActionTree<State, State> & Actions = {
  [ActionTypes.INC_COUNTER]({ commit }, payload: number) {
    commit(MutationTypes.INC_COUNTER, payload)
  },
}
// getters

export type Getters = {
  doubleCounter(state: State): number
}

export const getters: GetterTree<State, State> & Getters = {
  doubleCounter: (state) => state.counter * 2,
}

export const store = createStore({
  state,
  mutations,
  actions,
  plugins: [createLogger()],
})
