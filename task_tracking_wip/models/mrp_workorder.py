# -*- coding: utf-8 -*-
# © 2017 Comunitea Servicios Tecnológicos S.L. (http://comunitea.com)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api


class MrpWorkorder(models.Model):
    _inherit = 'mrp.workorder'

    @api.multi
    def _get_related_project(self):
        """
        Search related sale of procurement group to get the project
        """
        for wo in self:
            project_id = False
            if wo.production_id:
                project_id = wo.production_id.project_wip_id.id
            wo.project_wip_id = project_id

    task_id = fields.Many2one('project.task', 'Task', readonly=True)
    project_wip_id = fields.Many2one('project.project', 'Initial Project',
                                     compute='_get_related_project')

    @api.model
    def create(self, vals):
        track_model = self.env['tracking.wip']
        res = super(MrpWorkorder, self).create(vals)
        track_record = track_model.get_track_for_model(res._name, res)
        if track_record:
            track_record.create_task_tracking(res)
        return res

    # @api.multi
    # def write(self, vals):
    #     """
    #     Propagate to task da date expected to date end
    #     """
    #     res = super(StockMove, self).write(vals)
    #     if 'date_expected' in vals:
    #         for move in self:
    #             if move.task_id and \
    #                     move.task_id.date_end != move.date_expected:
    #                 move.task_id.date_end = move.date_expected
    #     return res

    @api.multi
    def action_cancel(self):
        """
        Remove related task when cancel sale order
        """
        res = super(MrpWorkorder, self).action_cancel()
        self.mapped('task_id').unlink()
        return res
