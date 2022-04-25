/* istanbul ignore file */
/* tslint:disable */
/* eslint-disable */

export type SubmitRequest = {
    /**
     * The blocks to run
     */
    blocks: string;
    /**
     * Whether to perform a full refresh
     */
    full_refresh?: boolean;
    /**
     * Whether to force a run even if a job with the same ID is already running
     */
    force?: boolean;
};
