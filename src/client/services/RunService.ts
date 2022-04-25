/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */
import type { SubmitRequest } from '../models/SubmitRequest';
import type { SubmitResponse } from '../models/SubmitResponse';

import type { CancelablePromise } from '../core/CancelablePromise';
import { OpenAPI } from '../core/OpenAPI';
import { request as __request } from '../core/request';

export class RunService {

    /**
     * Get Run
     * @param xMeltanoTraceId
     * @param xMeltanoEnv
     * @returns any Successful Response
     * @throws ApiError
     */
    public static getRunRunGet(
        xMeltanoTraceId: string,
        xMeltanoEnv: string,
    ): CancelablePromise<any> {
        return __request(OpenAPI, {
            method: 'GET',
            url: '/run/',
            headers: {
                'x-meltano-trace-id': xMeltanoTraceId,
                'x-meltano-env': xMeltanoEnv,
            },
            errors: {
                404: `Not found`,
                422: `Validation Error`,
            },
        });
    }

    /**
     * Submit Run
     * @param xMeltanoTraceId
     * @param xMeltanoEnv
     * @param requestBody
     * @returns SubmitResponse Successful Response
     * @throws ApiError
     */
    public static submitRunRunPost(
        xMeltanoTraceId: string,
        xMeltanoEnv: string,
        requestBody: SubmitRequest,
    ): CancelablePromise<SubmitResponse> {
        return __request(OpenAPI, {
            method: 'POST',
            url: '/run/',
            headers: {
                'x-meltano-trace-id': xMeltanoTraceId,
                'x-meltano-env': xMeltanoEnv,
            },
            body: requestBody,
            mediaType: 'application/json',
            errors: {
                404: `Not found`,
                422: `Validation Error`,
            },
        });
    }

}