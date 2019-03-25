import { Action } from 'redux';

import { BASE_API_URL } from '../../constants/api';
import { getProjectUrlFromName } from '../../constants/utils';
import { stdHandleError } from '../utils';
import { actionTypes } from './actionTypes';

export interface StartProjectTensorboardRequestAction extends Action {
  type: actionTypes.START_PROJECT_TENSORBOARD_REQUEST;
  projectName: string;
}

export interface StartProjectTensorboardSuccessAction extends Action {
  type: actionTypes.START_PROJECT_TENSORBOARD_SUCCESS;
  projectName: string;
}

export interface StartProjectTensorboardErrorAction extends Action {
  type: actionTypes.START_PROJECT_TENSORBOARD_ERROR;
  statusCode: number;
  error: any;
  projectName: string;
}

export function startProjectTensorboardRequestActionCreator(projectName: string): StartProjectTensorboardRequestAction {
  return {
    type: actionTypes.START_PROJECT_TENSORBOARD_REQUEST,
    projectName
  };
}

export function startProjectTensorboardSuccessActionCreator(projectName: string): StartProjectTensorboardSuccessAction {
  return {
    type: actionTypes.START_PROJECT_TENSORBOARD_SUCCESS,
    projectName
  };
}

export function startProjectTensorboardErrorActionCreator(statusCode: number,
                                                          error: any,
                                                          projectName: string): StartProjectTensorboardErrorAction {
  return {
    type: actionTypes.START_PROJECT_TENSORBOARD_ERROR,
    statusCode,
    error,
    projectName
  };
}

export interface StopProjectTensorboardRequestAction extends Action {
  type: actionTypes.STOP_PROJECT_TENSORBOARD_REQUEST;
  projectName: string;
}

export interface StopProjectTensorboardSuccessAction extends Action {
  type: actionTypes.STOP_PROJECT_TENSORBOARD_SUCCESS;
  projectName: string;
}

export interface StopProjectTensorboardErrorAction extends Action {
  type: actionTypes.STOP_PROJECT_TENSORBOARD_ERROR;
  statusCode: number;
  error: any;
  projectName: string;
}

export function stopProjectTensorboardRequestActionCreator(projectName: string): StopProjectTensorboardRequestAction {
  return {
    type: actionTypes.STOP_PROJECT_TENSORBOARD_REQUEST,
    projectName
  };
}

export function stopProjectTensorboardSuccessActionCreator(projectName: string): StopProjectTensorboardSuccessAction {
  return {
    type: actionTypes.STOP_PROJECT_TENSORBOARD_SUCCESS,
    projectName
  };
}

export function stopProjectTensorboardErrorActionCreator(statusCode: number,
                                                         error: any,
                                                         projectName: string): StopProjectTensorboardErrorAction {
  return {
    type: actionTypes.STOP_PROJECT_TENSORBOARD_ERROR,
    statusCode,
    error,
    projectName
  };
}

export type TensorboardProjectAction =
  StartProjectTensorboardRequestAction
  | StartProjectTensorboardSuccessAction
  | StartProjectTensorboardErrorAction
  | StopProjectTensorboardRequestAction
  | StopProjectTensorboardSuccessAction
  | StopProjectTensorboardErrorAction;

export function startTensorboard(projectName: string): any {
  return (dispatch: any, getState: any) => {
    const projectUrl = getProjectUrlFromName(projectName, false);

    dispatch(startProjectTensorboardRequestActionCreator(projectName));

    return fetch(`${BASE_API_URL}${projectUrl}/tensorboard/start`, {
      method: 'POST',
      headers: {
        'Authorization': 'token ' + getState().auth.token,
        'X-CSRFToken': getState().auth.csrftoken
      }
    })
      .then((response) => stdHandleError(
        response,
        dispatch,
        startProjectTensorboardErrorActionCreator,
        'Project not found',
        'Failed to start tensorboard for project',
        [projectName]))
      .then(() => {
        return dispatch(startProjectTensorboardSuccessActionCreator(projectName));
      });
  };
}

export function stopTensorboard(projectName: string): any {
  return (dispatch: any, getState: any) => {
    const projectUrl = getProjectUrlFromName(projectName, false);

    dispatch(stopProjectTensorboardRequestActionCreator(projectName));

    return fetch(`${BASE_API_URL}${projectUrl}/tensorboard/stop`, {
      method: 'POST',
      headers: {
        'Authorization': 'token ' + getState().auth.token,
        'X-CSRFToken': getState().auth.csrftoken
      }
    })
      .then((response) => stdHandleError(
        response,
        dispatch,
        stopProjectTensorboardErrorActionCreator,
        'Project not found',
        'Failed to start tensorboard for project',
        [projectName]))
      .then(() => {
        return dispatch(stopProjectTensorboardSuccessActionCreator(projectName));
      });
  };
}