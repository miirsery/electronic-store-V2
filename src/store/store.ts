import {
  ActionContext,
  ActionTree,
  createLogger,
  createStore,
  GetterTree,
  MutationTree,
  Store as VuexStore,
} from 'vuex'

export type State = { counter: number }

const state: State = { counter: 0 }

export enum MutationTypes {
  INC_COUNTER = 'SET_COUNTER',
}

export enum ActionTypes {
  INC_COUNTER = 'SET_COUNTER',
}

export type Mutations<S = State> = {
  [MutationTypes.INC_COUNTER](state: S, payload: number): void
}

// define mutations
const mutations: MutationTree<State> & Mutations = {
  [MutationTypes.INC_COUNTER](state: State, payload: number) {
    state.counter += payload
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
// export const store = createStore({
//   state,
//   mutations: {
//     increment(state, payload) {
//       state.counter++
//     },
//   },
//   actions: {
//     increment({ commit }) {
//       commit('increment')
//     },
//   },
// })
